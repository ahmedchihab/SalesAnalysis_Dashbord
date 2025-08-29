import pandas as pd

file_path = "cleaned_sales_data_final.csv"
df = pd.read_csv(file_path)



# Aperçu des premières lignes
print(df.head())

# Infos sur les colonnes et types
print(df.info())


# Statistiques descriptives pour les colonnes numériques
print(df.describe())

# Statistiques pour les colonnes object
print(df.describe(include=['object']))

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Conversion en datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Conversion de Quantity Ordered en entier
df['Quantity Ordered'] = df['Quantity Ordered'].astype(int)


# Supprimer les doublons (si plusieurs fois le même Order ID + Product)
df.drop_duplicates(inplace=True)

# Vérifier les valeurs manquantes
print(df.isnull().sum())
df.dropna(inplace=True)


# Extraire mois et année depuis Order Date
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year


print(df.dtypes)


# Sauvegarde dataset propre
df.to_csv(r"C:\Users\Galaxy\Downloads\SalesAnalysis_Portfolio\cleaned_sales_data_final.csv", index=False)

print("✅ Données nettoyées et sauvegardées")


