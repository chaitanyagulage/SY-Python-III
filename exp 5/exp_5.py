class LCSFinder:
    """A class to find the Longest Common Subsequence between two strings/sequences."""
    
    @staticmethod
    def find_lcs(sequence1, sequence2):
        """
        Computes the Longest Common Subsequence using Dynamic Programming.
        
        Args:
            sequence1 (str): The first sequence.
            sequence2 (str): The second sequence.
            
        Returns:
            tuple: (The LCS string, length of the LCS)
        """
        m = len(sequence1)
        n = len(sequence2)

        # 1. Initialize a DP table of size (m+1) x (n+1) with all zeros
        # dp[i][j] will store the length of LCS of sequence1[0..i-1] and sequence2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 2. Build the DP table in a bottom-up fashion
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, add 1 to the result of the previous diagonal cell
                if sequence1[i - 1] == sequence2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # If they don't match, take the maximum from the cell above or the cell to the left
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The bottom-right cell contains the length of the LCS
        lcs_length = dp[m][n]

        # 3. Reconstruct the actual LCS string by backtracking through the table
        # We start from the bottom-right corner and work our way back
        lcs_chars = [""] * lcs_length
        index = lcs_length - 1
        
        i, j = m, n
        while i > 0 and j > 0:
            # If characters match, this character is part of the LCS
            if sequence1[i - 1] == sequence2[j - 1]:
                lcs_chars[index] = sequence1[i - 1]
                i -= 1
                j -= 1
                index -= 1
            # If not, move in the direction of the larger value
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
                
        # Join the list of characters back into a string
        lcs_string = "".join(lcs_chars)
        
        return lcs_string, lcs_length


# ==========================================
# Example Usage (Driver Code)
# ==========================================
if __name__ == "__main__":
    # Example 1: DNA Sequence Comparison (Bioinformatics)
    dna1 = "AGGTAB"
    dna2 = "GXTXAYB"
    
    print("--- Example 1: Bioinformatics (DNA Comparison) ---")
    print(f"Sequence 1: {dna1}")
    print(f"Sequence 2: {dna2}")
    
    lcs_dna, length_dna = LCSFinder.find_lcs(dna1, dna2)
    print(f"Longest Common Subsequence: '{lcs_dna}'")
    print(f"Length: {length_dna}\n")
    
    # Example 2: Text/File Comparison (Diff tools like Git)
    text1 = "STONE"
    text2 = "LONGEST"
    
    print("--- Example 2: Text Comparison ---")
    print(f"Word 1: {text1}")
    print(f"Word 2: {text2}")
    
    lcs_text, length_text = LCSFinder.find_lcs(text1, text2)
    print(f"Longest Common Subsequence: '{lcs_text}'")
    print(f"Length: {length_text}")