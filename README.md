# WildlifeAPI

WildlifeAPI is a comprehensive and modular solution designed to interact with the Queensland Government's WildlifeNet API. It allows users to easily retrieve wildlife data with ease and efficiency.

## Features

- Modular design: Easily integrate with other systems or use as a standalone tool.
- Comprehensive data retrieval: Access a wide range of data from the WildlifeNet API.
- User-friendly: Designed with a focus on usability, making it easy to retrieve and understand the data.

## Getting Started

> 👉 Download code

```bash
git clone https://github.com/NathanPerrier/WildlifeAPI
cd WildlifeAPI
```

> 👉 Unrestrict **current user** scope   

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force;
```

> 👉 Install **python** modules via `VENV`  

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

> 👉 Run the **demo.py** file  

```bash
python demo.py
```

## Usage

> To search for a species use

```bash
Species(species='whiting').species_search()
```

> To find any group of species user

```bash
Species(species="fish").species_search()
```

> Retreive all class names

```bash
Classes().get_class_names()
```

> Optional Variables

```bash
debug | True/False | displays errors and urls
extensive_search | True/False | provides data for nested urls
extensive_info | provides additional info for a species (only works with species)
kingdom | str | change the kingdom from animals
```

## Built With

* [Python](https://www.python.org/) - The primary programming language used.

## Authors

* **Nathan Perrier** | [Github](https://github.com/NathanPerrier)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- [WildlifeNet](https://www.qld.gov.au/environment/plants-animals/species-information/wildnet)
- [QLD Wildlife API](https://www.data.qld.gov.au/dataset/qld-wildlife-data-api)
