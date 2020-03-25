# SES-DataCollector
Data collection app for SES workshop. The goal of this program is to collect data on every SES job run through the shop, organize and store that data into a spreadsheet, and send it to engineering for review. This is basically a clone of the VisualBasic/Excel program currently used. However, I believe it can be done better in Python. There are several bugs in the current VisualBasic implementation and it also runs very slowly. I plan to fix both of these problems in my python version.

## Procedure/flow

The general process flow of the program should go something like this, from the user perspective:

- start job
  - collect job info:
    - order #
    - part #
    - qty ordered
  - collect material info
    - stock OD
    - stock ID
    - material
    - stock qty
  - run job:
    - good parts?
      - enter qty good
    - scrap parts?
      - enter qty scrap
      - enter scrap code
    - need more stock?
      - add extra stock qty
  - **exit job**
    - return stock to inventory? y/n
      - yes: enter qty
      - no: continue
    - enter more good/scrap parts? good/scrap/no
      - good: enter qty
      - bad: enter qty & scrap code
      - no: continue
    - perform final calculations, store to CSV, send to engineering.