import matplotlib.pyplot as plt

def visualize_garden(garden):
    plt.clf()  # Clear the current figure
    plant_names = [plant.name for plant in garden.plants]
    growth_stages = [plant.growth_stage for plant in garden.plants]

    plt.bar(plant_names, growth_stages)
    plt.xlabel('Plant')
    plt.ylabel('Growth Stage')
    plt.title('Garden Growth Visualization')
    plt.draw()
    plt.pause(0.01)  # Pause to allow the figure to update
