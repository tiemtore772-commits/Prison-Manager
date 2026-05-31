
  Prison Manager: 

A Python-based prison management system built as a group project for the
Programming I course at Burkina Institute of Technology (BIT), May 2026.


 Project Description:

Prison Manager is a terminal-based application that allows prison staff
to manage detainees, cells, finances, trial dates, statistics, and archives.
The system is designed to simulate real-world prison administration operations.

 How to Run the Project:

.Requirements
- Python 3.10 or higher
- No external libraries required (only built-in modules)

.Steps

1. Clone the repository:
https://github.com/tiemtore772/Prison-Manager.git
2. Navigate to the project folder:
Prison-Manager
3. Run the program:
python main.py

 Features:

-  Add, search, and delete detainees
-  Create cells and assign detainees to cells
-  Record bail payments and view financial balance
-  Set and consult trial dates
-  View global prison statistics
-  Archive closed detainee files
-  Save and load all data

 Technologies Used:

 .Language
- Python 3.10+

 .Built-in Modules Used
- `datetime` — used to record entry dates, trial dates, and archive dates
- `random`   — used to automatically generate unique detainee IDs

 Projet Structure:

 .Prison-Manager

 main.py          → Main navigation menu 
 ______________________________________________________
 detainees.py     → Add / Search / Delete detainees 
 ______________________________________________________
 cell.py          → Create cells and assign detainees 
 ______________________________________________________
 finances.py      → Record bail and view balance 
 ______________________________________________________
 archives.py      → Archive closed files 
 ______________________________________________________
 data.py          → Save and load data 
 ______________________________________________________
 README.md        → Project
 ______________________________________________________

 

 Structure:
 ______________________________________________________________________________________________________
 Class             File         Inherits From   Key Methods
 ______________________________________________________________________________________________________
 `Personne`     `detainees.py`  None            `afficher_infos()`    
 ______________________________________________________________________________________________________
 `Detainers`    `detainees.py`  `Personne`      `display_info()`, `to_dict()`  
 ______________________________________________________________________________________________________
 `Cellule`      `cell.py`       None            `ajouter_detenu()`, `retirer_detenu()`, `est_pleine()` 
 ______________________________________________________________________________________________________
 `Caution`      `finances.py`   None            `mark_as_paid()`, `display()`, `to_dict()`    
 ______________________________________________________________________________________________________
 `Proces`       `date.py`       None            `fixer_date()`, `consulter()`                          
 ______________________________________________________________________________________________________
 `Archive`      `archives.py`   None            `archiver_dossier()`, `consulter_archive()`            
 ______________________________________________________________________________________________________

  Principles Demonstrated:

- **Encapsulation** → Private attributes (`__nom`, `__age`) accessed only
  via getters and setters
- **Abstraction** → Complex logic hidden behind simple methods like
  `liberer()` and `archiver()`
- **Inheritance** → `Detainers` inherits from `Personne`
- **Polymorphism** → `display_info()` behaves differently in `Personne`
  versus `Detainers`


  Group Members:
____________________________________________________________________________________
│ Member               │  Role                 │         GitHub Profile             │
│______________________│_______________________│____________________________________│
│ TIEMTORE Inoussa     │Leader_main.py         │      github.com/tiemtore772        │
│______________________│_______________________│____________________________________│
│ SOUGOTI Johan        │ detainees.py          │     github.com/johansougoti        │
│ _____________________│_______________________│____________________________________│
│ TOUGOUMA Emmanullela │  cell.py              │      github.com/emmatougouma843-afk│
│ _____________________│_______________________│____________________________________│
│ TOE Cynthia          │  finances.py          │      github.com/TOECynthia         │
│ _____________________│_______________________│____________________________________│
│ ZOUNGRANA Telesphore │  data.py              │      github.com/telesphore-hub     │
│ _____________________│_______________________│____________________________________│
│ TALL Bintou          │  archives.py          │      github.com/bint55tami-cpu     │
│______________________│_______________________│____________________________________│

 Acknowledgements:

. Python Official Documentation :https://docs.python.org/3/
. PEP 8 Style Guide :https://pep8.org/
. Burkina Institute of Technology — Programming I Course (3PRG1205)
. Lecturer: Kweyakie Afi BleboTechnologies Used
