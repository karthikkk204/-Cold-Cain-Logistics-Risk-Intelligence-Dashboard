# 🚛 Cold Cain Logistics & Risk Intelligence Dashboard

An end-to-end telemetry and risk analytics platform built in Power BI to monitor real-time temperature stability, track route excursion risks, and analyze supply chain loss metrics across perishable freight networks.

---

## 📌 Executive Summary

Maintaining strict thermal control during transit is critical for perishable goods such as pharmaceuticals, fresh produce, dairy, and frozen foods. This project provides supply chain operations teams with actionable, telemetry-driven intelligence to identify high-risk shipping corridors, quantify temperature excursion frequency, and minimize food loss before destination delivery.

---

## 📊 Key Features & Visualizations

* **Executive KPI Panel:** Tracks macro metrics including **Total Shipments**, **Total Excursions**, **Excursion Rate (%)**, and **Total Distance Covered (km)**.
* **Telemetry & Temperature Stability:** Analyzes internal container thermal fluctuations over time to flag breaches outside safety thresholds.
* **Route Risk Profiling:** Maps shipment distance and location hubs (`LOC_BLR`, `LOC_CHN`, `LOC_MUM`, etc.) against excursion occurrences to highlight problematic transit corridors.
* **Commodity Loss Breakdown:** Evaluates product integrity and loss percentages categorized by commodity types (*Fresh Produce*, *Dairy*, *Pharmaceuticals*, *Frozen Goods*).
* **Interactive Slicers:** Dynamic regional and operational filtering by origin, destination, commodity, and timeline.

---

## 🛠️ Tech Stack & Methods

* **Business Intelligence:** Power BI Desktop, DAX (Data Analysis Expressions), Data Modeling (Star Schema)
* **Data Transformation:** Power Query, M Code, Data Cleaning & Normalization
* **Analytics & Metrics:**
  * **Excursion Rate %:**  
    $$\text{Excursion Rate} = \frac{\text{Total Excursion Shipments}}{\text{Total Shipments}} \times 100$$
  * **Average Internal Temperature ($^\circ\text{C}$):** Aggregated telemetry readings per shipment leg.

---

## 📂 Project Structure

```
├── data/
│   ├── cold_chain_telemetry.csv      # Telemetry sensor log data
│   └── route_master.xlsx             # Origin-destination distance matrix
├── pbix/
│   └── cold_chain_analysis.pbix      # Main Power BI Report file
├── screenshots/
│   └── dashboard_overview.png        # Dashboard screenshot
└── README.md                         # Project documentation
```

---

## 📈 Key Insights & Recommendations

1. **High-Risk Corridors:** Transit routes passing through `LOC_HYD` and `LOC_MUM` exhibited higher average excursion rates during extended transit stops.
2. **Commodity Sensitivity:** *Fruits* and *Vegetables* registered the highest food loss percentages, warranting improved pre-cooling procedures and route optimization.
3. **Preventive Action:** Implementing automated thermal alerts when internal temperature strays past $\pm 2^\circ\text{C}$ of baseline reduces spoilage risk significantly.

---


