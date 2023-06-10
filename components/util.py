import pandas as pd

def read_file():
  df = pd.read_csv('/Users/marielydelacruz/code/sleep_study/Sleep_health_and_lifestyle_dataset.csv')
  df.loc[df['BMI Category'] == 'Normal Weight', 'BMI Category'] = 'Normal'
  df["Sleep Disorder"].fillna("No Sleep Disorder", inplace = True)
  return df

def get_gender_sleep_avg():
  df = read_file()
  gender_score = df.groupby('Gender')[['Quality of Sleep']].mean()
  gender_score.reset_index(inplace=True)
  return gender_score

def get_occupation_sleep_avg():
  df = read_file()
  occupation_score = df.groupby('Occupation')[['Quality of Sleep']].mean()
  occupation_score.reset_index(inplace=True)
  return occupation_score

def get_age_sleep_avg():
  df = read_file()
  age_score = df.groupby('Age')[['Quality of Sleep']].mean()
  age_score.reset_index(inplace=True)
  return age_score

def get_gender_duration_avg():
  df = read_file()
  gender_score = df.groupby('Gender')[['Sleep Duration']].mean()
  gender_score.reset_index(inplace=True)
  return gender_score

def get_occupation_duration_avg():
  df = read_file()
  occupation_score = df.groupby('Occupation')[['Sleep Duration']].mean()
  occupation_score.reset_index(inplace=True)
  return occupation_score

def get_age_duration_avg():
  df = read_file()
  age_score = df.groupby('Age')[['Sleep Duration']].mean()
  age_score.reset_index(inplace=True)
  return age_score

def get_gender_exercise_avg():
  df = read_file()
  gender_score = df.groupby('Gender')[['Physical Activity Level']].mean()
  gender_score.reset_index(inplace=True)
  return gender_score

def get_occupation_exercise_avg():
  df = read_file()
  occupation_score = df.groupby('Occupation')[['Physical Activity Level']].mean()
  occupation_score.reset_index(inplace=True)
  return occupation_score

def get_age_exercise_avg():
  df = read_file()
  age_score = df.groupby('Age')[['Physical Activity Level']].mean()
  age_score.reset_index(inplace=True)
  return age_score

def get_gender_stress_level_avg():
  df = read_file()
  gender_score = df.groupby('Gender')[['Stress Level']].mean()
  gender_score.reset_index(inplace=True)
  return gender_score

def get_occupation_stress_level_avg():
  df = read_file()
  occupation_score = df.groupby('Occupation')[['Stress Level']].mean()
  occupation_score.reset_index(inplace=True)
  return occupation_score

def get_age_stress_level_avg():
  df = read_file()
  age_score = df.groupby('Age')[['Stress Level']].mean()
  age_score.reset_index(inplace=True)
  return age_score

def sleep_quality_count():
  df = read_file()
  percentages = df['Quality of Sleep'].value_counts()
  return percentages

def stress_level_count():
  df = read_file()
  percentages = df['Stress Level'].value_counts()
  return percentages

def bmi_count():
  df = read_file()
  percentages = df['BMI Category'].value_counts()
  return percentages

def sleep_disorder_count():
  df = read_file()
  percentages = df['Sleep Disorder'].value_counts(dropna=False)
  return percentages