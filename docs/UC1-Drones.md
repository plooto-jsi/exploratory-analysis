# ITALIAN USE CASE - Drones - CFRP

## Readme

The purpose of this document is to aggregate all the core info about use case in order to allow anyone to get an instant and detailed overview of the work progress.


## Partners

* AUEB - Optimization
  * K(ostas?) Kapari
* TUC - Process modelling
* JSI - Data-driven modelling
* HP Composites - providing materials
* CETMA - providing materials
* CETMA Composites - re-testing and curing materials
  * Silvio Pappada
* Acceli - drone production, use case leader
  * Sevasti Gioti (use case leader) 

## Use case definition

Use case 1 is divided into these cases:

* discretization/classification of uncured material
* classification of cured materials
* (UCC3) Z


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
