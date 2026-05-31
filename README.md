# Prison Manager

A Python-based prison management system built as a group project for the
Programming I course at Burkina Institute of Technology (BIT), May 2026.

---

##  Project Description

BIT Prison Manager is a terminal-based application that allows prison staff
to manage detainees, cells, finances, trial dates, statistics, and archives.
The system is designed to simulate real-world prison administration operations.

---

##  How to Run the Project

### Requirements

| Item | Details |
|------|---------|
| Language | Python 3.10 or higher |
| Libraries | No external libraries required |
| Modules | Built-in modules only |

### Steps

| Step | Command |
|------|---------|
| 1. Clone the repository | `git clone https://github.com/tiemtore772/Prison-Manager.git` |
| 2. Navigate to the folder | `cd Prison-Manager` |
| 3. Run the program | `python main.py` |

---

##  Features

| # | Feature |
|---|---------|
| 1 |  Add, search, and delete detainees |
| 2 |  Create cells and assign detainees to cells |
| 3 |  Record bail payments and view financial balance |
| 4 |  Set and consult trial dates |
| 5 |  View global prison statistics |
| 6 |  Archive closed detainee files |
| 7 |  Save and load all data |

---

## Technologies Used

| Type | Details |
|------|---------|
| Language | Python 3.10+ |
| `datetime` | Used to record entry dates, trial dates, and archive dates |
| `random` | Used to automatically generate unique detainee IDs |

---

##  Project Structure

| File | Description |
|------|-------------|
| `main.py` | Main navigation menu |
| `detainees.py` | Add / Search / Delete detainees |
| `cell.py` | Create cells and assign detainees |
| `finances.py` | Record bail and view financial balance |
| `archives.py` | Archive closed detainee files |
| `data.py` | Save and load data |
| `README.md` | Project documentation |

---

##  OOP Structure

| Class | File | Inherits From | Key Methods |
|-------|------|---------------|-------------|
| `Personne` | `detainees.py` | None | `afficher_infos()` |
| `Detainers` | `detainees.py` | `Personne` | `display_info()`, `to_dict()` |
| `Cellule` | `cell.py` | None | `ajouter_detenu()`, `retirer_detenu()`, `est_pleine()` |
| `Caution` | `finances.py` | None | `mark_as_paid()`, `display()`, `to_dict()` |
| `Proces` | `date.py` | None | `fixer_date()`, `consulter()` |
| `Archive` | `archives.py` | None | `archiver_dossier()`, `consulter_archive()` |

### OOP Principles Demonstrated

| Principle | How it is applied |
|-----------|------------------|
| **Encapsulation** | Private attributes (`__nom`, `__age`) accessed only via getters and setters |
| **Abstraction** | Complex logic hidden behind simple methods like `liberer()` and `archiver()` |
| **Inheritance** | `Detainers` inherits from `Personne` |
| **Polymorphism** | `display_info()` behaves differently in `Personne` versus `Detainers` |

---

##  Group Members

| Member | Role | GitHub Profile |
|--------|------|----------------|
| TIEMTORE Inoussa | Leader — `main.py` | [tiemtore772](https://github.com/tiemtore772) |
| SOUGOTI Johan | `detainees.py` | [johansougoti](https://github.com/johansougoti) |
| TOUGOUMA Emmanuella | `cell.py` | [emmatougouma843-afk](https://github.com/emmatougouma843-afk) |
| TOE Cynthia | `finances.py` | [TOECynthia](https://github.com/TOECynthia) |
| ZOUNGRANA Telesphore | `data.py` | [telesphore-hub](https://github.com/telesphore-hub) |
| TALL Bintou | `archives.py` | [bint55tami-cpu](https://github.com/bint55tami-cpu) |

---

##  Acknowledgements

| Resource | Link |
|----------|------|
| Python Official Documentation | [docs.python.org](https://docs.python.org/3/) |
| PEP 8 Style Guide | [pep8.org](https://pep8.org/) |
| Course | Burkina Institute of Technology — 3PRG1205 |
| Lecturer | Kweyakie Afi Blebo |
