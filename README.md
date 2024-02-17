# Automation-of-Data-Visualization

This web application, created with Streamlit, offers a range of features designed to enhance data visualization and plotting. It aids in a deeper understanding of various aspects of your data.
<p align="center">
  <img src="https://github.com/oussama-hammami/Automation-of-data-visualization/blob/main/img/previw.png" width = "800" height = "400">
</p>

* [Requirements](#requirements)
* [App Core](#app-code)

## Requirements

To install the necessary dependencies, run:

```python
pip install -r requirements.txt
```
## App Core

To utilize this app, run:
```python
streamlit run main.py
```
you can drag and drop your file into the designated area or use the browse button to access your file.

Initially, the app displays a header of the data, including column names and some sample entries. Following this, it presents a series of Select and Text Input boxes.

Based on an analysis of each column's values, these boxes are assigned as follows:

If the data can be categorized into a few distinct categories, a sliding box will be assigned to the corresponding column.

If the data comprises many unique values and cannot be easily categorized, an input box will be assigned. This input box allows users to enter a condition, 
enabling them to apply filters on the corresponding columns for more refined data selection.
