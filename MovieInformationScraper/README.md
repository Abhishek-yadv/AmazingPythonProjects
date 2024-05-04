Sure, here's a documented README file with the steps explained, without including the actual code:

# Data Cleaning in SQL

This README file provides a step-by-step guide to cleaning and transforming data using SQL queries. The code examples are based on the "NashvilleHousing" dataset, but the techniques can be applied to any dataset that requires data cleaning and manipulation.

## Table of Contents

1. [Standardize Date Format](#standardize-date-format)
2. [Populate Property Address Data](#populate-property-address-data)
3. [Break Out Address into Individual Columns](#break-out-address-into-individual-columns)
4. [Change Y and N to Yes and No](#change-y-and-n-to-yes-and-no)
5. [Remove Duplicates](#remove-duplicates)
6. [Delete Unused Columns](#delete-unused-columns)

### Standardize Date Format

In this step, we convert the `SaleDate` column from its original format to a standardized date format (`yyyy-mm-dd`). This process involves creating a new column `SaleDateConverted` and updating it with the converted date values.

### Populate Property Address Data

This step handles missing or null values in the `PropertyAddress` column. We self-join the table on `ParcelID` and populate the null `PropertyAddress` values with the corresponding non-null values from the other rows with the same `ParcelID`.

### Break Out Address into Individual Columns

Here, we split the `PropertyAddress` and `OwnerAddress` columns into separate address, city, and state columns. This is done using string manipulation functions like `SUBSTRING`, `CHARINDEX`, `PARSENAME`, and `REPLACE`.

### Change Y and N to Yes and No

In this step, we update the `SoldAsVacant` column by replacing the 'Y' and 'N' values with 'Yes' and 'No', respectively, using a `CASE` statement.

### Remove Duplicates

This section deals with removing duplicate rows from the dataset. We use a `ROW_NUMBER` window function to identify and remove duplicate rows based on a combination of columns (`ParcelID`, `PropertyAddress`, `SalePrice`, `SaleDate`, and `LegalReference`). The duplicate rows are identified using a common table expression (CTE) and then deleted from the table.

### Delete Unused Columns

In the final step, we remove any unnecessary or unused columns from the dataset using the `ALTER TABLE` and `DROP COLUMN` statements.

Note: The code examples provided are specific to the "NashvilleHousing" dataset. You may need to modify the column names and table names to fit your dataset. Additionally, make sure to create a backup of your data before running any queries that modify the data.
