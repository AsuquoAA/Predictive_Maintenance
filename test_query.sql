-- Step 8: Check if query is now properly optimized

---- Analyze query performance with EXPLAIN ANALYZE
EXPLAIN ANALYZE 
WITH 

---- Aggregate Pressure readings by CycleID, storing them as an array
Pressure_Agg AS (
    SELECT CycleID, ARRAY_AGG(Pressure_data) AS Pressure_Readings 
    FROM Pressure 
    GROUP BY CycleID
),

---- Aggregate Temperature readings by CycleID, storing them as an array
Temperature_Agg AS (
    SELECT CycleID, ARRAY_AGG(Temperature_data) AS Temperature_Readings 
    FROM Temperature 
    GROUP BY CycleID
),

---- Aggregate Flow Sensor readings by CycleID, storing them as an array
Flow_Agg AS (
    SELECT CycleID, ARRAY_AGG(Flow_Sensor_data) AS Flow_Sensor_Readings 
    FROM Flow_Sensor 
    GROUP BY CycleID
),

---- Aggregate Stable Efficiency readings by CycleID, storing them as an array
Stable_Agg AS (
    SELECT CycleID, ARRAY_AGG(Stable_Efficiency_data) AS Stable_Efficiency_Readings 
    FROM Stable_Efficiency 
    GROUP BY CycleID
),

---- Aggregate Cooling Efficiency readings by CycleID, storing them as an array
Cooling_Eff_Agg AS (
    SELECT CycleID, ARRAY_AGG(Cooling_Efficiency_data) AS Cooling_Efficiency_Readings 
    FROM Cooling_Efficiency 
    GROUP BY CycleID
),

---- Aggregate Cooling Power readings by CycleID, storing them as an array
Cooling_Power_Agg AS (
    SELECT CycleID, ARRAY_AGG(Cooling_Power_data) AS Cooling_Power_Readings 
    FROM Cooling_Power 
    GROUP BY CycleID
),

---- Aggregate Vibration Sensor readings by CycleID, storing them as an array
Vibration_Agg AS (
    SELECT CycleID, ARRAY_AGG(Vibration_Sensor_data) AS Vibration_Sensor_Readings 
    FROM Vibration_Sensor 
    GROUP BY CycleID
),

---- Aggregate Efficiency Power Signal readings by CycleID, storing them as an array
Efficiency_Agg AS (
    SELECT CycleID, ARRAY_AGG(Efficiency_Power_Signal_data) AS Efficiency_Power_Signal_Readings 
    FROM Efficiency_Power_Signal 
    GROUP BY CycleID
)

---- Final query to join all aggregated tables with the Cycle table
SELECT 
    c.CycleID,                      
    p.Pressure_Readings,            
    t.Temperature_Readings,         
    fs.Flow_Sensor_Readings,        
    se.Stable_Efficiency_Readings,  
    ce.Cooling_Efficiency_Readings, 
    cp.Cooling_Power_Readings,      
    vs.Vibration_Sensor_Readings,   
    eps.Efficiency_Power_Signal_Readings, 
    pf.Cooler_Condition,            
    pf.Valve_Condition,             
    pf.Pump_Leakage,                
    pf.Accumulator_Condition,       
    pf.Stable_Flag            
FROM Cycle c
INNER JOIN Pressure_Agg p ON c.CycleID = p.CycleID
INNER JOIN Temperature_Agg t ON c.CycleID = t.CycleID
INNER JOIN Flow_Agg fs ON c.CycleID = fs.CycleID
INNER JOIN Stable_Agg se ON c.CycleID = se.CycleID
INNER JOIN Cooling_Eff_Agg ce ON c.CycleID = ce.CycleID
INNER JOIN Cooling_Power_Agg cp ON c.CycleID = cp.CycleID
INNER JOIN Vibration_Agg vs ON c.CycleID = vs.CycleID
INNER JOIN Efficiency_Agg eps ON c.CycleID = eps.CycleID
INNER JOIN Profile pf ON c.CycleID = pf.CycleID; 