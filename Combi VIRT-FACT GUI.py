import streamlit as st

def trouver_combinaisons(virements, cible, tolerance=0.01):
    resultats = []
    virements.sort()  # tri croissant

    def backtrack(start, chemin, total):
        if abs(total - cible) <= tolerance:
            resultats.append(list(chemin))
            return
        if total > cible + tolerance:
            return
        for i in range(start, len(virements)):
            if i > start and virements[i] == virements[i - 1]:
                continue
            if total + virements[i] > cible + tolerance:
                break
            chemin.append(virements[i])
            backtrack(i + 1, chemin, total + virements[i])
            chemin.pop()


    backtrack(0, [], 0.0)
    return resultats

# Interface Streamlit
st.title("🔎 Rapprochement de Virements / Factures")
st.write("Trouvez toutes les combinaisons possibles de montants pour atteindre une somme cible.")

# Saisie des montants
saisie = st.text_area("Entrez les montants séparés par des espaces (ex: 100.25 50.00 23.75)", height=150)
cible_input = st.text_input("Entrez la somme cible (ex: 150.00)")

if st.button("Lancer la recherche"):

    try:
        virements = list(map(lambda x: float(x.replace(",", ".")), saisie.strip().split()))
        cible = float(cible_input.replace(",", "."))
        virements = [v for v in virements if v <= cible + 0.01]

        if not virements:
            st.warning("Aucun montant n'est inférieur ou égal à la somme cible.")
        else:
            st.success(f"{len(virements)} montants pris en compte (≤ {cible:.2f} €). Recherche en cours...")
            combinaisons = trouver_combinaisons(virements, cible)

            if not combinaisons:
                st.error("❌ Aucune combinaison ne permet d’atteindre la somme cible.")
            else:
                st.success(f"✅ {len(combinaisons)} combinaison(s) trouvée(s) :")
                for i, comb in enumerate(combinaisons, 1):
                    expression = " + ".join(f"{v:.2f}" for v in comb)
                    st.write(f"**{i}.** {expression} = **{cible:.2f} €**")

    except ValueError:
        st.error("Erreur dans la saisie : veuillez entrer uniquement des nombres valides.")

# Note : lancer avec : 
#streamlit run "/Users/nolhan/Documents/Python/Combi VIRT-FACT GUI.py"
