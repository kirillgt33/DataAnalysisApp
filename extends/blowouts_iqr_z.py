import numpy as np

# Нахождение выбросов по методу Тьюки
def outliers_iqr_mod(data, feature, left=1.5, right=1.5, log_scale=False):
            if log_scale:
                x = np.log(data[feature])
            else:
                x = data[feature]
            quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
            iqr = quartile_3 - quartile_1
            lower_bound = quartile_1 - (iqr * left)
            upper_bound = quartile_3 + (iqr * right)
            outliers = data[(x < lower_bound) | (x > upper_bound)]
            cleaned = data[(x >= lower_bound) & (x <= upper_bound)]
            return outliers, cleaned

# Нахождение выбросов по методу z-отклонений
def outliers_z_score_mod(data, feature, log_scale=False, left=3, right=3):
            if log_scale:
                x = np.log(data[feature]+1)
            else:
                x = data[feature]
            mu = x.mean()
            sigma = x.std()
            lower_bound = mu - left * sigma
            upper_bound = mu + right * sigma
            outliers = data[(x < lower_bound) | (x > upper_bound)]
            cleaned = data[(x >= lower_bound) & (x <= upper_bound)]
            return outliers, cleaned