import pandas as pd
from lifelines import CoxPHFitter

# sample survival dataset
data = pd.DataFrame({
    "time": [5, 8, 12, 18, 23, 34, 45, 54, 62, 76],
    "event": [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    "age": [60, 67, 70, 55, 73, 65, 62, 69, 57, 64],
    "treatment": [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
})
import pandas as pd
from lifelines import CoxPHFitter

# sample survival dataset
data = pd.DataFrame({
    "time": [5, 8, 12, 18, 23, 34, 45, 54, 62, 76],
    "event": [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    "age": [60, 67, 70, 55, 73, 65, 62, 69, 57, 64],
    "treatment": [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
})

# fit Cox model
cph = CoxPHFitter()
cph.fit(data, duration_col="time", event_col="event")

# summary
print(cph.summary)

# hazard ratio for each covariate
print("HR(age) =", np.exp(cph.params_["age"]))
print("HR(treatment) =", np.exp(cph.params_["treatment"]))

# optional: prediction for new patient
new = pd.DataFrame({"age":[66, 72], "treatment":[1, 0]})
pred = cph.predict_survival_function(new)
print(pred.head())
# fit Cox model
cph = CoxPHFitter()
cph.fit(data, duration_col="time", event_col="event")

# summary
print(cph.summary)

# hazard ratio for each covariate
print("HR(age) =", np.exp(cph.params_["age"]))
print("HR(treatment) =", np.exp(cph.params_["treatment"]))

# optional: prediction for new patient
new = pd.DataFrame({"age":[66, 72], "treatment":[1, 0]})
pred = cph.predict_survival_function(new)
print(pred.head())
