# Smart Tourist Route Planning Tool

## Brief Description

This project features an **intelligent tourist route planning tool**. Based on user input—such as starting point, ending point, required/optional/forbidden attractions, and constraints (time, distance, cost)—the tool automatically calculates the optimal travel route. It can be used for travel assistance decisions, route recommendations, and automated itinerary planning in a web frontend or other applications.

## Main Features

- **Data Cleaning and Integration:**  
  `pt.py`, `taxi.py`, and `merge_data.py` are used for cleaning and merging raw data files related to attractions and transportation.

- **Data Extraction Module:**  
  `data.py` is responsible for extracting and organizing data for later route planning.

- **Route Planning Core:**  
  `route.py` implements the main route planning logic. To facilitate integration with a frontend web application, it uses JSON files for both input and output.

- **User Input Example:**  
  `user_input.json` contains sample user input information for route planning as follows:
```json
{
    "start": "The Forbidden City",          // Starting point
    "end": "Temple of Heaven",              // Ending point
    "must_visit": ["Summer Palace", "Shichahai"], // Required attractions
    "can_visit": [],                        // Optional attractions (visited only if within limits)
    "not_visit": ["Badaling Great Wall"],   // Forbidden attractions (will not visit)
    "max_time": 180,                        // Maximum total time (minutes)
    "max_dist": 50.0,                       // Maximum total distance (km)
    "max_price": 200.0,                     // Maximum total price (CNY)
    "mode": "time"                          // Planning criterion: can be "distance" (shortest distance), "time" (shortest time), or "price" (lowest cost)
}
```

## Example Output

Below is an example of the planned route and result based on the above input:

```json
{
  "route": [                 // The sequence of attractions to visit
    "The Forbidden City",
    "Shichahai",
    "Summer Palace",
    "Temple of Heaven"
  ],
  "steps": [                 // The detailed segment info between each pair
    {
      "from": "The Forbidden City",
      "to": "Shichahai",
      "public_transport_route": "Tian'anmen West Station (Line 1) → Nanpu Station (Line 1→Line 8) → Shichahai Station (Line 8)",
      "distance_km": 2.0,
      "time_min": 15,
      "taxi_price_yuan": 13.0
    },
    {
      "from": "Shichahai",
      "to": "Summer Palace",
      "public_transport_route": "Shichahai Station (Line 8) → Nanpu Station (Line 8→Line 1) → Xidan Station (Line 1→Line 4) → Summer Palace Station (Line 4)",
      "distance_km": 14.3,
      "time_min": 45,
      "taxi_price_yuan": 60.0
    },
    {
      "from": "Summer Palace",
      "to": "Temple of Heaven",
      "public_transport_route": "Summer Palace Station (Line 4) → Xidan Station (Line 4→Line 1) → Dongdan Station (Line 1→Line 5) → Temple of Heaven East Gate Station (Line 5)",
      "distance_km": 20.0,
      "time_min": 50,
      "taxi_price_yuan": 55.0
    }
  ],
  "total_time_min": 110.0,      // Total time required (minutes)
  "total_distance_km": 36.3,    // Total distance traveled (km)
  "total_price_yuan": 128.0,    // Total taxi fare (CNY)
  "success": true               // Whether a feasible route is found
}

```

# Front-end

## Front-end Display Module

* Technology stack: Vite + ECharts (data visualization) + Element UI (component library)

* Core functions: route result display, attraction data visualization

## Front-end Project Files


| File / Directory Path                         | 	Function Description          |
| --------------------------------------------- | -------------- |
| `src/pages/home/home.vue`                     | Front-end homepage (user demand input interface) |
| `src/pages/scenicAreaData/scenicAreaData.vue` | Attraction data display page        |
| `src/figure`                                  | Directory for storing image resources needed by the front-end webpage |
| `package-lock.json`                           | Front-end project dependency configuration file    |

## Usage Instructions

### Front-end Running Steps



1. **Dependency Installation**: Enter the root directory of the front-end project and execute the following command to install dependencies (Node.js needs to be installed in advance):


```
npm install
```



1. **Local Running**: After the dependencies are installed, execute the following command to start the local service:



```
npm run dev
```



1. **Page Access**：After successful startup, access the front-end page according to the local address prompted in the terminal (such as http://127.0.0.1:5173/)

2. **Page Switching**：Switch between the "Home" and "Beijing Scenic Area Data" through the top navigation bar


# Notes

1. The front-end project only supports local running and has not been deployed on a server. It needs to be accessed by starting a local service through npm run dev

2. Before running the front-end, ensure that the Node.js environment is installed, and dependencies are installed through package-lock.json (to avoid version conflicts)