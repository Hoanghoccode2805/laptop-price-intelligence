#Step 1: Environment Setup & Library Import
library(tidyverse) 
library(scales) 

#Step 2: Data Preprocessing & Type Casting
laptops_final$RAM_GB <- as.numeric(laptops_final$RAM_GB)
laptops_final$SSD_GB <- as.numeric(laptops_final$SSD_GB)
laptops_final$Price <- as.numeric(laptops_final$Price)
str(laptops_final)

#Step 3: Market Share Analysis (Brand Volume)
p1 <- laptops_final %>%
  count(Brand) %>%                              
  mutate(Brand = fct_reorder(Brand, n)) %>%      
  
  ggplot(aes(x = n, y = Brand)) +                
  geom_col(fill = "steelblue", width = 0.7) +    
  geom_text(aes(label = n), hjust = -0.2, size = 4) +      
  scale_x_continuous(expand = expansion(mult = c(0, 0.3))) +
  labs(
    title = "Laptop Market Share by Brand",
    subtitle = "Number of available models per brand",
    x = "Count",
    y = NULL,                                   
    caption = "Source: laptops_final"
  ) +
  
  theme_minimal() +                              
  theme(
    panel.grid.major.y = element_blank(),       
    plot.title = element_text(face = "bold", size = 14) 
  )

print(p1)

# Step 4: Price Segmentation Analysis (Boxplot)
p2 <- laptops_final %>%
  filter(!is.na(Brand)) %>%
  mutate(Brand = fct_reorder(Brand, Price, .fun = median)) %>% 
  ggplot(aes(x = Brand, y = Price, fill = Brand)) +
  geom_boxplot(alpha = 0.6, outlier.colour = "red", outlier.shape = 1) + 
  
  scale_y_continuous(labels = label_dollar(prefix = "", suffix = " €")) + 
  
  labs(
    title = "Price Distribution by Brand",
    subtitle = "Price range comparison (Min, Median, Max) across manufacturers",
    x = NULL,   # Brand names are self-explanatory
    y = "Price",
    caption = "Sorted by median price"
  ) +
  
  theme_light() +
  theme(
    legend.position = "none", # Hide legend (redundant)
    axis.text.x = element_text(angle = 45, hjust = 1, size = 10, face = "bold"), 
    panel.grid.major.x = element_blank()
  )

print(p2)


# Step 5: Feature Correlation Analysis (Price vs. RAM)
p3 <- laptops_final %>%
  ggplot(aes(x = Price, y = RAM_GB)) +
  
  geom_point(aes(color = Brand), size = 3, alpha = 0.7) + 
  
  geom_smooth(method = "lm", color = "black", linetype = "dashed", se = FALSE) + 

  coord_cartesian(ylim = c(0, 150), xlim = c(0, 9000)) + 

  scale_x_continuous(labels = label_dollar(prefix = "", suffix = " €")) +
  scale_y_continuous(breaks = c(8, 16, 32, 64, 128)) +

  labs(
    title = "Correlation: Price vs. RAM Configuration",
    subtitle = "Trend analysis: Higher specs generally correlate with higher prices",
    x = "Price",
    y = "RAM (GB)",
    color = "Manufacturer"
  ) +
  
  theme_minimal() +
  theme(
    legend.position = "bottom",         
    legend.box.background = element_rect(color = "gray", linewidth = 0.5), 
    plot.subtitle = element_text(color = "gray40", face = "italic")
  )

print(p3)
