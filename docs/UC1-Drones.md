# ITALIAN PILOT - Drones - CFRP

## Readme
`UNDER CONSTRUCTION`
The purpose of this document is to aggregate all the core info about use case in order to allow anyone to get an instant and detailed overview of the work progress.


## Partners

* AUEB - Optimization
  * K(ostas?) Kapari
* TUC - Process modelling
  * Tsinarakis Gerogios
* JSI - Data-driven modelling
* HP Composites - providing materials
* CETMA - providing materials
* CETMA Composites - re-testing and curing materials
  * Silvio Pappada
* Acceli - drone production, use case leader
  * Sevasti Gioti (use case leader) 

## Use case definition

Pilot 1 is divided into these data-driven modeling use cases:

* classification of uncured material
* classification of cured materials

Scraps before going to CETMA have some unknown properties, such as residual life (depends on thermal history of starting prepreg that comes from HP).
Prepreg is identified by code.
This code identifies resin code, resin properties, carbon properties.
The prepreg scraps that are in HPC have this kind of info.
Modelling (process and data-driven) will mainly help to estimate re-qualification.
They are also measuring energy consumption during the process (Silvio). 
This might be an idea for modelling.
They would experiment on the different ways of material treatment (e. g. heating) wrt energy consumption.

The material that go from CC back to HPC is total scrap. We want to completely minimize that. If materials at CETMA fail the tests, these are scrap. Need to be thrown away.
Use of energy is the main optimization function for this use case!

Qs:
* How does CETMA requalify the prepreg?
* Thermal history of the prepreg can change ??? HOW?
* From one prepreg we can have different requalified pre-preg, using different processes.
* Modelling: good estimation regarding requalification.
* Different kind of process optimizations.
* Are there different requalification processes? CETMA requalification process is aimed to study the resin. They don't do requalification of the fibers or other kind of requalification. Basically, they find the new properties of the resin. They can use the expired roles in the small pieces (like plates, not tubes).
* There is a CIRCE project - Circular Economy Model for Carbon Fiber Prepregs - information from there would be quite useful.




### Data availability

`TODO`
Information about historic data and data that will be available.

The parameters that influence the use case are:

* parameter 1
* parameter 2
* parameter 3

Any other  relevant info.

### I/O definition
`TODO`

All the inputs have a datetime stamp and ...

| Expected Inputs | | | |
| --- | --- | --- | --- |
| Inputs description | Input | Unit | Freq |
| Specific inputs | Temperature | Celsius degrees °C | Hourly |
|                 | Pressure | kPa | Hourly |
|                 | ... | | |
| Environmental   | Relative humidity | % | Hourly |
|                 | Temperature | °C | Hourly |
|                 | ... | | |
| Weather data    | Wind Speed | m/s | Hourly |
|                 | ... | | |

All the outputs have a datetime stamp as well as location ID, that refer to a specific box.

| Expected Outputs | | | |
| --- | --- | --- | --- |
| Outputs description | Output | Unit | Freq |
| Sensor prediction | datetimes, values | None | Daily |
