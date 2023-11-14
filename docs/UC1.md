# USE CASE 1

## Readme

The purpose of this document is to aggregate all the core info about use case in order to allow anyone to get an instant and detailed overview of the work progress.


## Partners

* List of involved partners, contacts, roles

## Use case definition

Use case 1 is divided into these cases:

* (UCC1) X
* (UCC2) Y
* (UCC3) Z

## UCC1 case

UCC1 refers to _"This task"_.

Short description of the use case.

UCC1 goals are:

* Goal 1
* Goal 2
* Goal 3

### Data availability

Information about historic data and data that will be available.

The parameters that influence the use case are:

* parameter 1
* parameter 2
* parameter 3

Any other  relevant info.

### I/O definition

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
