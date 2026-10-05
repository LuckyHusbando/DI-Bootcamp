#DC - Challenge - Gold DNA

import random

# The fundamental unit of heredity
class Gene:
    def __init__(self, value=0):
        self.value = value

    def mutate(self):
        """Flips the gene's value."""
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)

# A series of 10 genes
class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        """Randomly mutates a subset of its genes."""
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to flip
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)
    
    def __repr__(self):
        return f"[{''.join(str(gene) for gene in self.genes)}]"

# A series of 10 chromosomes
class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        """Randomly mutates a subset of its chromosomes."""
        for chromosome in self.chromosomes:
            if random.random() < 0.5:  # 50% chance for a chromosome to mutate
                chromosome.mutate()

    def is_perfect(self):
        """Checks if all genes in all chromosomes are 1s."""
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __repr__(self):
        return f"DNA:\n" + "\n".join(f"  {i}: {chromo}" for i, chromo in enumerate(self.chromosomes))

# An organism with a DNA and an environmental mutation probability
class Organism:
    def __init__(self, environment_prob):
        self.dna = DNA()
        self.environment_prob = environment_prob

    def mutate(self):
        """Mutates the organism's DNA based on environmental probability."""
        if random.random() < self.environment_prob:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_perfect()
    
    def __repr__(self):
        return f"Organism with DNA:\n{self.dna}"

# --- Simulation ---
if __name__ == "__main__":
    # Instantiate a number of organisms with an environmental mutation probability
    environment_probability = 0.2
    organisms = [Organism(environment_probability) for _ in range(5)]
    
    generations = 0
    winner = None

    print("Starting simulation...")
    while winner is None:
        generations += 1
        
        for i, organism in enumerate(organisms):
            organism.mutate()
            if organism.is_perfect():
                winner = i
                break
        
        # Optional: Print progress every 1000 generations
        if generations % 1000 == 0:
            print(f"Generation {generations}: No perfect DNA yet.")
            
    print("\n--- Simulation Complete ---")
    print(f"Organism {winner} achieved perfect DNA after {generations} generations!")
    print(organisms[winner])
    