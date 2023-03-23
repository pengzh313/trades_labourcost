---
editor_options: 
  markdown: 
    wrap: 72
---

# Motivation and Purpose

It is a great opportunity to apply what we have learned from the UBC MDS
DSCI-532 Data Visualization II course to start to solve practical
problems that were seen from students' previous workplaces. This
`trade_labourcost` Dash data-visualization App project is created based
on the author's previous working experiences. The App will be
continuously improved to add more industrial data and features to better
reflect the expectations from the estimators in the construction
industries in Canada.

**Target audience**: Upon adding more practical features, the app will
become a handy tool for estimators who working in the construction
industry to receive the quick insights about labour costing of various
trades in different scheduling scenarios.

# Description of the data

The raw data came from the author's previous work in Manitoba, Canada.
They were originally extracted and processed from the publicly available
wage and benefit schedule of union collective agreements. **In the
current stage as of March 22, 2023, the result can only be used when
working with trades people from four union locals in Canada: Boilermaker
Local 555, Millwright Local 1443, Ironworkers Local 728, and Pipefitter
Local 254**. Since there are hundreds trades union locals across Canada,
we are planning to expand the app usage to cover more union locals in
the future.

The raw data `labour_rates` included in the `data` folder of the repo
have three sheets:

-   Sheet 1: rates.\
    There are three columns in the table. The first column lists four
    types of trades. The second column indicates three commonly used
    wage times in the construction industry in Canada. `st` for straight
    time; `ot` for overtime; and `dt` for double time. Then the third
    column shows corresponding labour hourly rates in Canadian dollars.

Note that the hourly rates include wage and benefit according to the
union agreements, and on top of them, all the employer responsible
CPP/EI contributions have also been added. The rates can be considered
as a gross labour cost from the employer side. Therefore, estimators can
easily use the data and calculated weekly costs when deal with labour
cost estimating.

-   Sheet 2: shift.\
    This table included four commonly used work shifts for a typical
    construction project. For example, 5d_8h refers to work 8 hours a
    day, 5 days a week; 6d_10h means to work 10 hours a day, 6 days a
    week (including Saturdays). For different trades, there might be
    different definition of overtime and double time. The table has
    listed combinations of definition for trades and shifts to capture
    the differences that would be beneficial for estimators to deal with
    the complexity.

-   Sheet 3: LOA.\
    This table includes the daily LOA (Living out allowance) for four
    trades as per three defined travel zone. Similar as the second
    sheet, this is to capture the differences from trades and make
    estimators' job easier when they have to work with various unions on
    a daily basis. The data from sheet 3 has not been utilized for the
    current stage of app development. We will keep updating the app and
    add more features in the future.

# Primary research question and usage scenarios

The project aims to answer the following primary question:

`As a project estimator in the construction industry, what is the weekly labour cost for different scenarios when dealing with various trades and shift schedule?`.

This seems like a simple question to be answered. However, when dealing
with a large number of trade unions that all have different rates and
conditions, a quick tool is needed for estimators to play with different
scenarios and figure out best options for a particular project.
Considering the magnitude of dollar values for a typical construction
project, the cost saving or efficiency improvement driven from the App
could be significant.

Below is an example of a usage scenario from a member of our target
audience.

John is an estimator working for a construction company that is
specialized to provide trades services, such as millwrighting, boiler
building/repair, structural steel erection, and piping system
installation/repair, etc. As one of the main responsibilities, he
performs the cost estimating for projects that the company are bidding
for. Most of the projects require multiple trades from different union
locals. All these locals supply trades members based on their own
pre-negotiated agreements with specific wage/benefit rates and
conditions. Unfortunately, there is no consistence in this industry.
Previously, John had made mistakes many times when he adopted wrong
rates or made the messy calculations in the MS Excel spreadsheet. After
John started to use the `trade_labourcost` app, he found it as a handy
tool for his regular work. By selecting the desired trade, he is able to
quickly compare the weekly labour costs for four different shift
arrangement. And he know the value have already included payroll costs
from the employer side so he would never need to add extra formula in
the Excel to manually calculate these expected expenses. In addition, by
selecting the dropdown options of four common work shifts, the gross
labour costs for trades are available in the output table. John is
satisfied with the continence from the App and look forward to more
features to be implemented in the future.
