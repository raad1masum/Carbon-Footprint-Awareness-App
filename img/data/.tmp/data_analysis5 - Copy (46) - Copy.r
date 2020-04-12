install.packages("dslabs")

library(dslabs)

if(!require("tidyverse")) install.packages("tidyverse")
if(!require("ggrepel")) install.packages("ggrepel")
if(!require("matrixStats")) install.packages("matrixStats")

library(tidyverse)
library(ggrepel)
library(matrixStats)

colorblind_palette <- c("black", "#E69F00", "#56B4E9", "#009E73", "#CC79A7", "#F0E442", "#0072B2", "#D55E00")

data(temp_carbon)

# line plot of annual global, land and ocean temperature anomalies since 1880
temp_carbon %>%
  select(Year = year, Global = temp_anomaly, Land = land_anomaly, Ocean = ocean_anomaly) %>%
  gather(Region, Temp_anomaly, Global:Ocean) %>%
  ggplot(aes(Year, Temp_anomaly, col = Region)) +
  geom_line(size = 1) +
  geom_hline(aes(yintercept = 0), col = colorblind_palette[8], lty = 2) +
  geom_label(aes(x = 2005, y = -.08), col = colorblind_palette[8], 
             label = "20th century mean", size = 4) +
  ylab("Temperature anomaly (degrees C)") +
  xlim(c(1880, 2018)) +
  scale_color_manual(values = colorblind_palette) +
  ggtitle("Temperature anomaly relative to 20th century mean, 1880-2018")

data(greenhouse_gases)

# line plots of atmospheric concentrations of the three major greenhouse gases since 0 CE
greenhouse_gases %>%
  ggplot(aes(year, concentration)) +
  geom_line() +
  facet_grid(gas ~ ., scales = "free") +
  xlab("Year") +
  ylab("Concentration (CH4/N2O ppb, CO2 ppm)") +
  ggtitle("Atmospheric greenhouse gas concentration by year, 0-2000 CE")

# line plot of anthropogenic carbon emissions over 250+ years
temp_carbon %>%
  ggplot(aes(year, carbon_emissions)) +
  geom_line() +
  xlab("Year") +
  ylab("Carbon emissions (metric tons)") +
  ggtitle("Annual global carbon emissions, 1751-2014")

data(historic_co2)

# line plot of atmospheric CO2 concentration over 800K years, colored by data source
historic_co2 %>%
  ggplot(aes(year, co2, col = source)) +
  geom_line() +
  ylab("CO2 (ppm)") +
  scale_color_manual(values = colorblind_palette[7:8]) +
  ggtitle("Atmospheric CO2 concentration, -800,000 BCE to today")