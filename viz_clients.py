import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv(
    "clients_clustered.csv",
    names=["client_id", "nb_achats", "montant_total", "score_fidelite", "categorie"]
)

# Conversion en nombres si nécessaire
df["score_fidelite"] = pd.to_numeric(df["score_fidelite"], errors="coerce")
df["montant_total"] = pd.to_numeric(df["montant_total"], errors="coerce")

# Style Seaborn moderne
sns.set(style="whitegrid", palette="pastel")

plt.figure(figsize=(12, 7))

# Scatter plot : couleur par catégorie
sns.scatterplot(
    data=df,
    x="montant_total",
    y="score_fidelite",
    hue="categorie",
    size="nb_achats",
    sizes=(50, 300),
    alpha=0.8,
    palette="Set2"
)

plt.title("Segmentation des Clients : Montant vs Fidélité", fontsize=16)
plt.xlabel("Montant total des achats", fontsize=12)
plt.ylabel("Score de fidélité", fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid(True)
plt.tight_layout()
plt.show()
