class KnapsackSolver:
    """A class to solve the 0/1 Knapsack Problem using Dynamic Programming."""

    @staticmethod
    def solve_top_down(weights, values, capacity):
        """
        Top-Down Approach (Recursion with Memoization).
        Starts from the full capacity and total items, breaking the problem down.
        """
        n = len(values)
        # Initialize memoization table with -1 (indicating uncalculated states)
        # Dimensions: (n + 1) x (capacity + 1)
        memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

        def knapsack_recursive(w, i):
            # Base Case: No items left or capacity is 0
            if i == 0 or w == 0:
                return 0
            
            # If this subproblem has already been solved, return the cached result
            if memo[i][w] != -1:
                return memo[i][w]

            # If the current item's weight exceeds capacity, we MUST skip it
            if weights[i - 1] > w:
                memo[i][w] = knapsack_recursive(w, i - 1)
            else:
                # We have a choice:
                # 1. Include the item (add its value, and subtract its weight from capacity)
                # 2. Exclude the item (move to the next item, capacity remains same)
                include_item = values[i - 1] + knapsack_recursive(w - weights[i - 1], i - 1)
                exclude_item = knapsack_recursive(w, i - 1)
                
                # Store and return the maximum of the two choices
                memo[i][w] = max(include_item, exclude_item)

            return memo[i][w]

        # Start the recursion from the maximum capacity and the last item
        return knapsack_recursive(capacity, n)


    @staticmethod
    def solve_bottom_up(weights, values, capacity):
        """
        Bottom-Up Approach (Iteration with Tabulation).
        Builds the solution from base cases (0 capacity/items) up to the target.
        """
        n = len(values)
        # Initialize a DP table with 0s
        # dp[i][w] represents the max value using the first 'i' items with a weight limit of 'w'
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Build table in bottom-up manner
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                # If current item's weight is less than or equal to current capacity
                if weights[i - 1] <= w:
                    # Max of: (Value of current item + max value of remaining capacity) OR (Not taking the item)
                    include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                    exclude_item = dp[i - 1][w]
                    
                    dp[i][w] = max(include_item, exclude_item)
                else:
                    # Item is too heavy, we must exclude it
                    dp[i][w] = dp[i - 1][w]

        # The bottom-right cell contains the maximum value for the full constraints
        max_value = dp[n][capacity]
        
        # --- Optional: Reconstruct the optimal item selection ---
        selected_items = []
        w = capacity
        for i in range(n, 0, -1):
            # If the value came from the cell above, the item was NOT included
            if dp[i][w] != dp[i - 1][w]:
                selected_items.append(i - 1)  # Store the index of the included item
                w -= weights[i - 1]           # Reduce remaining capacity
                
        selected_items.reverse() # Reverse to show in original order
        
        return max_value, selected_items


# ==========================================
# Example Usage (Driver Code)
# ==========================================
if __name__ == "__main__":
    # Problem definition
    item_values = [60, 100, 120]
    item_weights = [10, 20, 30]
    max_capacity = 50
    
    print(f"Items (Values):  {item_values}")
    print(f"Items (Weights): {item_weights}")
    print(f"Knapsack Capacity: {max_capacity} kg\n")

    # 1. Test Top-Down Approach
    print("--- Top-Down (Memoization) ---")
    max_val_td = KnapsackSolver.solve_top_down(item_weights, item_values, max_capacity)
    print(f"Maximum Value Achieved: ${max_val_td}\n")

    # 2. Test Bottom-Up Approach
    print("--- Bottom-Up (Tabulation) ---")
    max_val_bu, chosen_indices = KnapsackSolver.solve_bottom_up(item_weights, item_values, max_capacity)
    
    print(f"Maximum Value Achieved: ${max_val_bu}")
    print("Selected Items (0-indexed):", chosen_indices)
    
    # Detail the selected items
    print("\nDetailed Selection:")
    total_weight = 0
    for idx in chosen_indices:
        print(f" - Item {idx}: Weight = {item_weights[idx]}kg, Value = ${item_values[idx]}")
        total_weight += item_weights[idx]
    print(f"Total Weight Used: {total_weight}kg / {max_capacity}kg")