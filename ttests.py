import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pandas as pd

#Generate dataframe to represent physical activity levels for men vs women

genders = ["Male", "Female"]
gender = np.random.choice(genders, size = 1000)
df = pd.DataFrame({"Gender":gender})

def get_activity(row):
    if row["Gender"] == "Male":
        return np.random.normal(150,50, size = 1)
    else:
        return np.random.normal(120,50, size = 1)

df["Active Minutes"] = df.apply(get_activity, axis=1)

phys_activity = []

for value in df["Active Minutes"].values:
    phys_activity.append(value.item())

df["Active Minutes"] = phys_activity

sns.displot(data = df, x = "Active Minutes", hue = "Gender", kind = "kde")
plt.show()

men = df.loc[df["Gender"] == "Male"]
women = df.loc[df["Gender"] == "Female"]

men_arr = men["Active Minutes"].to_numpy()
women_arr = women["Active Minutes"].to_numpy()

mean_men = np.mean(men_arr)
mean_women = np.mean(women_arr)
print("Average Weekly Exercise Time for Men %5.2f"%(mean_men))
print("Average Weekly Exercise Time for Women %5.2f"%(mean_women))

compare_means = stats.ttest_ind(men_arr,women_arr)
print(compare_means)


