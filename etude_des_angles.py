from calcul_angles import df_angles_Chrono250
from calcul_angles import df_angles_Chrono300
from calcul_angles import df_angles_Chrono350
from calcul_angles import df_angles_Route250
from calcul_angles import df_angles_Route300
from calcul_angles import df_angles_Route350

# On commence par étudier les maximum, le minimum et la différence maximum - minimum 
# pour Chrono250
for articulation in df_angles_Chrono250["Articulation"].unique():
    maximum = max(df_angles_Chrono250[df_angles_Chrono250["Articulation"] == articulation]["Angle"])
    minimum = min(df_angles_Chrono250[df_angles_Chrono250["Articulation"] == articulation]["Angle"])
    difference = maximum - minimum
    print(f"Maximum ({articulation}: {maximum})")
    print(f"Minimum ({articulation}: {minimum})")
    print(f"Difference max-min ({articulation}: {difference})")

# On le fait maintenant pour Chrono300
for articulation in df_angles_Chrono300["Articulation"].unique():
    maximum = max(df_angles_Chrono300[df_angles_Chrono300["Articulation"] == articulation]["Angle"])
    minimum = min(df_angles_Chrono300[df_angles_Chrono300["Articulation"] == articulation]["Angle"])
    difference = maximum - minimum
    print(f"Maximum ({articulation}: {maximum})")
    print(f"Minimum ({articulation}: {minimum})")
    print(f"Difference max-min ({articulation}: {difference})")

# Puis pour Chrono350
for articulation in df_angles_Chrono350["Articulation"].unique():
    maximum = max(df_angles_Chrono350[df_angles_Chrono350["Articulation"] == articulation]["Angle"])
    minimum = min(df_angles_Chrono350[df_angles_Chrono350["Articulation"] == articulation]["Angle"])
    difference = maximum - minimum
    print(f"Maximum ({articulation}: {maximum})")
    print(f"Minimum ({articulation}: {minimum})")
    print(f"Difference max-min ({articulation}: {difference})")

# On passe à Route250
for articulation in df_angles_Route250["Articulation"].unique():
    maximum = max(df_angles_Route250[df_angles_Route250["Articulation"] == articulation]["Angle"])
    minimum = min(df_angles_Route250[df_angles_Route250["Articulation"] == articulation]["Angle"])
    difference = maximum - minimum
    print(f"Maximum ({articulation}: {maximum})")
    print(f"Minimum ({articulation}: {minimum})")
    print(f"Difference max-min ({articulation}: {difference})")

# Puis on fait Route300
for articulation in df_angles_Route300["Articulation"].unique():
    maximum = max(df_angles_Route300[df_angles_Route300["Articulation"] == articulation]["Angle"])
    minimum = min(df_angles_Route300[df_angles_Route300["Articulation"] == articulation]["Angle"])
    difference = maximum - minimum
    print(f"Maximum ({articulation}: {maximum})")
    print(f"Minimum ({articulation}: {minimum})")
    print(f"Difference max-min ({articulation}: {difference})")

# On termine par Route350
for articulation in df_angles_Route350["Articulation"].unique():
    maximum = max(df_angles_Route350[df_angles_Route350["Articulation"] == articulation]["Angle"])
    minimum = min(df_angles_Route350[df_angles_Route350["Articulation"] == articulation]["Angle"])
    difference = maximum - minimum
    print(f"Maximum ({articulation}: {maximum})")
    print(f"Minimum ({articulation}: {minimum})")
    print(f"Difference max-min ({articulation}: {difference})")
