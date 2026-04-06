import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Visualizations:

    """
    This class groups all visualization methods used in Phase 3 of the assessment.
    It applies a consistent visual style across all charts.
    """

    def __init__(self, df):

        """
        Initialize the class with the dataset and configure the visual style.

        Parameters:
        -----------
        df : pandas DataFrame
            Cleaned dataset used for visualization.
        """

        self.df = df.copy()
        self.palette = "viridis"
        self.configure_style()

    def configure_style(self):

        """
        Apply a consistent visual style to all charts.
        """

        sns.set_theme(style="whitegrid")
        plt.rcParams["figure.figsize"] = (10, 6)
        plt.rcParams["axes.titlesize"] = 14
        plt.rcParams["axes.labelsize"] = 11
        plt.rcParams["xtick.labelsize"] = 10
        plt.rcParams["ytick.labelsize"] = 10

    def get_unique_customers(self, columns):

        """
        Return one row per customer for customer-level visualizations.

        The original dataset contains multiple records per customer (one per month),
        which would lead to duplicated individuals in analyses focused on customer
        attributes (e.g., province, salary, loyalty card).

        This function removes duplicate entries based on "Loyalty Number" to ensure
        that each customer is counted only once, preventing biased or inflated results.

        Parameters:
        -----------
        columns : list
            Columns to keep in the returned DataFrame.

        Returns:
        --------
        pandas DataFrame
            Dataset with unique customers only.
        """

        return self.df[columns].drop_duplicates(subset=["Loyalty Number"])

    def apply_plot_format(self, title, xlabel, ylabel, rotation=0):

        """
        Apply common formatting to charts.

        Parameters:
        -----------
        title : str
            Plot title.
        xlabel : str
            X-axis label.
        ylabel : str
            Y-axis label.
        rotation : int, optional
            Rotation angle for x-axis labels.
        """

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=rotation)
        plt.tight_layout()
        plt.show()

    def flights_booked_by_month(self):

        """
        Plot total flights booked by month.
        """

        monthly_flights = (self.df.groupby("Month", as_index=False)["Flights Booked"].sum().sort_values("Month"))

        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=monthly_flights,
            x="Month",
            y="Flights Booked",
            hue="Month",
            palette=self.palette,
            legend=False)
        
        self.apply_plot_format(
            title="Flights Booked by Month",
            xlabel="Month",
            ylabel="Total Flights Booked")

    def distance_vs_points(self):

        """
        Plot the relationship between distance and points accumulated.
        """

        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=self.df,
            x="Distance",
            y="Points Accumulated",
            alpha=0.3)
        
        self.apply_plot_format(
            title="Distance vs Points Accumulated",
            xlabel="Distance",
            ylabel="Points Accumulated")

    def customers_by_province(self):

        """
        Plot the number of unique customers by province.
        """

        unique_customers = self.get_unique_customers(["Loyalty Number", "Province"])

        province_counts = (
            unique_customers.groupby("Province", as_index=False)["Loyalty Number"]
            .count()
            .rename(columns={"Loyalty Number": "Customers"})
            .sort_values("Customers", ascending=False))

        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=province_counts,
            x="Province",
            y="Customers",
            hue="Province",
            palette=self.palette,
            legend=False)
        
        self.apply_plot_format(
            title="Number of Customers by Province",
            xlabel="Province",
            ylabel="Number of Customers",
            rotation=45)

    def salary_by_education(self):

        """
        Plot average salary by education level.
        """

        unique_customers = self.get_unique_customers(["Loyalty Number", "Education", "Salary"])

        salary_education = (
            unique_customers.groupby("Education", as_index=False)["Salary"]
            .mean()
            .sort_values("Salary", ascending=False))

        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=salary_education,
            x="Education",
            y="Salary",
            hue="Education",
            palette=self.palette,
            legend=False)
        
        self.apply_plot_format(
            title="Average Salary by Education Level",
            xlabel="Education Level",
            ylabel="Average Salary",
            rotation=45)

    def loyalty_card_proportion(self):

        """
        Plot the proportion of unique customers by loyalty card type.
        """

        unique_customers = self.get_unique_customers(["Loyalty Number", "Loyalty Card"])

        card_counts = unique_customers["Loyalty Card"].value_counts()
        colors = sns.color_palette(self.palette, len(card_counts))

        plt.figure(figsize=(8, 8))
        plt.pie(
            card_counts.values,
            labels=card_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors)
        
        plt.title("Proportion of Customers by Loyalty Card Type")
        plt.tight_layout()
        plt.show()

    def marital_status_by_gender(self):

        """
        Plot the distribution of unique customers by marital status and gender.
        """

        unique_customers = self.get_unique_customers(["Loyalty Number", "Marital Status", "Gender"])

        plt.figure(figsize=(10, 6))
        sns.countplot(
            data=unique_customers,
            x="Marital Status",
            hue="Gender",
            palette=self.palette)
        
        self.apply_plot_format(
            title="Customer Distribution by Marital Status and Gender",
            xlabel="Marital Status",
            ylabel="Number of Customers")