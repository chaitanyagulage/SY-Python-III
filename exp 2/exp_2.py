# ==========================================
# Decorators for Dynamic Formatting
# ==========================================
def add_borders(func):
    """Decorator that wraps the report output in a decorative border."""
    def wrapper(self, *args, **kwargs):
        content = func(self, *args, **kwargs)
        border = "=" * 50
        return f"{border}\n{content}\n{border}"
    return wrapper

def html_format(func):
    """Decorator that wraps the report output in basic HTML tags."""
    def wrapper(self, *args, **kwargs):
        content = func(self, *args, **kwargs)
        return f"<html>\n<body>\n{content}\n</body>\n</html>"
    return wrapper

# ==========================================
# Core Class Definition
# ==========================================
class Report:
    """A dynamic report generator showcasing advanced OOP concepts."""
    
    # Class attribute to track the total number of reports created
    _total_reports_generated = 0

    def __init__(self, title, body, author="Admin"):
        self.title = title
        self.body = body
        self.author = author
        Report._total_reports_generated += 1

    # --- Magic Methods (Dunder Methods) ---
    
    def __str__(self):
        """Defines the user-friendly string representation of the object."""
        return f"Report: '{self.title}' by {self.author}"

    def __len__(self):
        """Returns the length of the report's body text."""
        return len(self.body)

    def __add__(self, other):
        """Allows combining two reports using the '+' operator."""
        if isinstance(other, Report):
            combined_title = f"{self.title} & {other.title}"
            combined_body = f"{self.body}\n\n--- Added Section ---\n\n{other.body}"
            return Report(title=combined_title, body=combined_body, author="System Merged")
        raise TypeError("Unsupported operand type. Can only add two Report objects.")

    # --- Class Methods ---
    
    @classmethod
    def from_dictionary(cls, data_dict):
        """Alternative constructor: Creates a Report object from a dictionary."""
        return cls(
            title=data_dict.get('title', 'Untitled'),
            body=data_dict.get('body', 'No content provided.'),
            author=data_dict.get('author', 'Unknown')
        )

    @classmethod
    def get_total_reports(cls):
        """Returns the total number of reports instantiated."""
        return cls._total_reports_generated

    # --- Instance Methods with Decorators ---
    
    def generate_plain(self):
        """Generates the raw, unformatted report."""
        return f"TITLE: {self.title}\nAUTHOR: {self.author}\n\n{self.body}"

    @add_borders
    def generate_with_borders(self):
        """Generates the report wrapped in borders."""
        return self.generate_plain()

    @html_format
    @add_borders
    def generate_web_view(self):
        """Generates the report with borders, wrapped in HTML (stacked decorators)."""
        # Note: Decorators are applied bottom-to-top. 
        # add_borders runs first, then html_format wraps that result.
        return self.generate_plain()


# ==========================================
# Example Usage (Driver Code)
# ==========================================
if __name__ == "__main__":
    # 1. Standard Instantiation
    report1 = Report("Q1 Sales", "Sales increased by 15% in Q1.", "Alice")
    
    # 2. Using a Class Method (Alternative Constructor)
    data = {
        "title": "Q2 Projections", 
        "body": "Expecting a 5% drop due to supply chain issues.", 
        "author": "Bob"
    }
    report2 = Report.from_dictionary(data)

    # 3. Demonstrating Magic Methods
    print("--- Magic Methods ---")
    print(report1)                             # Triggers __str__
    print(f"Length of Report 1 body: {len(report1)} characters")  # Triggers __len__
    
    # Combining objects using __add__
    combined_report = report1 + report2        
    print(f"Combined Report Title: {combined_report.title}\n")

    # 4. Demonstrating Decorators
    print("--- Formatted Outputs (Decorators) ---")
    print("1. Bordered Format:")
    print(report1.generate_with_borders())
    print("\n2. Web Format (Stacked Decorators):")
    print(combined_report.generate_web_view())

    # 5. Demonstrating Class State
    print(f"\nTotal reports generated in system: {Report.get_total_reports()}")
