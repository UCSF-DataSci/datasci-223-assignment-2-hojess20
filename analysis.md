# Cohort Analysis Report

## Analysis Approach

To analyze patient health trends across different BMI groups, we used a dataset generated by `generate_large_health_data.py`, which includes 5 million records with synthetic noise in glucose and age values, as well as a diagnosis column derived from the outcome variable. This dataset was converted from a .csv file to a parquet file.

For data cleaning, I filtered out implausible BMI values (<10 or >60) to remove likely data entry errors. I then assigned patients to BMI categories using standard WHO ranges:
- Underweight: 10 ≤ BMI < 18.5  
- Normal: 18.5 ≤ BMI < 25  
- Overweight: 25 ≤ BMI < 30  
- Obese: 30 ≤ BMI ≤ 60  

And finally, for each BMI cohort, I calculated:
- Average glucose level (`avg_glucose`)
- Total number of patients (`patient_count`)
- Average age (`avg_age`)

## Summary Statistics

| BMI Range    | Avg Glucose | Patient Count | Avg Age |
|--------------|-------------|----------------|---------|
| Obese        | 126.03 mg/dL | 3,066,409       | 33.83 years |
| Underweight  | 95.20 mg/dL  | 26,041          | 23.98 years |
| Normal       | 108.00 mg/dL | 664,064         | 31.89 years |
| Overweight   | 116.37 mg/dL | 1,165,360       | 32.88 years |

## Insights
Glucose levels rise steadily across increasing BMI categories and it peaks in the Obese group at 126 mg/dL, which is a clinically significant threshold for elevated blood sugar. The Underweight cohort is younger on average and has the lowest glucose levels. This may reflect different metabolic dynamics or health behaviors. The majority of patients fall into the Obese and Overweight categories, suggesting an overweight-skewed population distribution in the dataset.

## Polars Usage
Polars was used for its fast and efficient performance with large datasets. Lazy evaluation through `scan_parquet()` allowed us to defer execution and chain multiple transformations without triggering intermediate computations. Pipeline chaining with `.pipe()` allowed us to structure the transformation process in a clear, modular way, where each stage in the pipeline focused on a single function (e.g., filtering, selecting, transforming, aggregating).

Overall, polars handled 5 million rows quickly and with low memory overhead, making it ideal for scalable health data processing.
