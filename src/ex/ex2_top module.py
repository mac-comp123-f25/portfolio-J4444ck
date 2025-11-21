import numpy as np
import pandas as pd
import pingouin as pg

# Example 1: One-sample t-test
# Test whether the mean of a sample is different from 0.

np.random.seed(1)
x = np.random.normal(loc=0.5, scale=1.0, size=30)

one_sample = pg.ttest(x=x, y=0, alternative="two-sided")
print("One-sample t-test (mean of x vs 0):")
print(one_sample, "\n")

print("One-sample details:")
print("  t        :", one_sample["T"].iloc[0])
print("  dof      :", one_sample["dof"].iloc[0])
print("  p-value  :", one_sample["p-val"].iloc[0])
print("  CI95%    :", one_sample["CI95%"].iloc[0])
print("  Cohen's d:", one_sample["cohen-d"].iloc[0])
print("  BF10     :", one_sample["BF10"].iloc[0])
print("  power    :", one_sample["power"].iloc[0], "\n")


# Example 2: Paired t-test (within-subjects)
# Pre/post scores from the same participants.

df_paired = pd.DataFrame({
    "subject": np.arange(1, 11),
    "pre":  [10, 9, 11, 8, 7, 9, 10, 8, 9, 7],
    "post": [12, 11, 12, 9, 8, 10, 11, 9, 10, 8]
})

paired_res = pg.ttest(x=df_paired["pre"],
                      y=df_paired["post"],
                      paired=True,
                      alternative="two-sided")
print("Paired t-test (pre vs post):")
print(paired_res, "\n")

print("Paired t-test details:")
print("  t        :", paired_res["T"].iloc[0])
print("  dof      :", paired_res["dof"].iloc[0])
print("  p-value  :", paired_res["p-val"].iloc[0])
print("  CI95%    :", paired_res["CI95%"].iloc[0])
print("  Cohen's d:", paired_res["cohen-d"].iloc[0])
print("  BF10     :", paired_res["BF10"].iloc[0])
print("  power    :", paired_res["power"].iloc[0], "\n")


# Example 3: Independent-samples t-test (between-subjects)
# Two groups: control vs treatment.

df_ind = pd.DataFrame({
    "group":   ["control"] * 12 + ["treatment"] * 12,
    "score":   [11, 10, 9, 12, 11, 10, 9, 8, 10, 11, 9, 10,
                13, 14, 12, 15, 13, 14, 12, 13, 14, 15, 13, 14]
})

x_ctrl = df_ind.query("group == 'control'")["score"]
x_treat = df_ind.query("group == 'treatment'")["score"]

ind_res = pg.ttest(x=x_ctrl,
                   y=x_treat,
                   paired=False,
                   alternative="two-sided")
print("Independent-samples t-test (control vs treatment):")
print(ind_res, "\n")

print("Independent t-test details:")
print("  t        :", ind_res["T"].iloc[0])
print("  dof      :", ind_res["dof"].iloc[0])
print("  p-value  :", ind_res["p-val"].iloc[0])
print("  CI95%    :", ind_res["CI95%"].iloc[0])
print("  Cohen's d:", ind_res["cohen-d"].iloc[0])
print("  BF10     :", ind_res["BF10"].iloc[0])
print("  power    :", ind_res["power"].iloc[0], "\n")


