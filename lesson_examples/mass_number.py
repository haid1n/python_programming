from collections import defaultdict

import re

# Simplified periodic table

atomic_weights = {
	"H": 1.008,
	"C": 12.011,
	"O": 15.999,
	"N": 14.007,
	"Na": 22.009,
	"Cl": 35.45,
	"Ca": 40.078,
	"Mg": 24.305,
	"Fe": 55.845
}

def calculate_molar_mass(chemical_formula: str) -> float:
	"""
	Calculates the molar mass of a compound given its chemical formula

	Parameters:
		chemical_formula(str) : The chemical formula (e.g, "H2O", "C6H12O6")

	Returns:
		float: The molar mass of the compound in g/mol

	"""

	matches = re.findall(r"([A-Z][a-z]*)(\d*)", chemical_formula)

	total_mass = 0.0


	for element, count in matches:
		if element not in atomic_weights:
			raise ValueError(f"Unknown element: {element}")

		atom_count = int(count) if count else 1

		total_mass += atomic_weights[element] * atom_count

	return total_mass

compound = "C6H12O6"

molar_mass = calculate_molar_mass(compound)

print(f"Molar mass of {compound}: {molar_mass} g/mol" )