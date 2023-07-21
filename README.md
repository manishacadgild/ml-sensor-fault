# ml-sensor-fault
Sensor-Fault-Detection:


Problem Statement

The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

Solution Proposed

In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

Step1. Create a conda environment after opening the repository
``` bash
conda create -p venv python==3.8 -y
````
``` bash
conda activate venv
``` 
``` bash MongoDB URL.
MONGO_DB_URL="mongodb+srv://mongodb:mongodb@mongodb.n1arurv.mongodb.net/?retryWrites=true&w=majority"
````
```bash
pip install ipykernel 
```

