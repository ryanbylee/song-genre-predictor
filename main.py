from dataloader import DataLoader
import matplotlib.pyplot as plt

def main():
    dataset = DataLoader([0,0,0])
    dataset.print_data_info()
    print("\n------\n")

    # plot the relationship between tempo and popularity
    plt.scatter(dataset.df['tempo'], dataset.df['popularity'], s=0.1)
    plt.xlabel('tempo')
    plt.ylabel('popularity')
    plt.title('tempo vs popularity')
    plt.savefig('tempo_vs_popularity.png')

    # plot the distirubtion of genre
    dataset.df['track_genre'].value_counts().plot(kind='bar')
    plt.xlabel('genre')
    plt.ylabel('count')
    plt.title('distribution of genre')
    plt.savefig('genre_distribution.png')

    # calcuate average popularity for each genre
    avg_popularity = dataset.df.groupby('track_genre')['popularity'].mean()
    # print top 5 with number of songs in each genre
    # iterate through the top 5 genres above and print the number of songs in each genre
    for genre in avg_popularity.sort_values(ascending=False).head(5).index:
        print(f"Average popularity in genre {genre}: {avg_popularity[genre]}, Number of songs: {dataset.df[dataset.df['track_genre'] == genre].shape[0]}")


if __name__ == '__main__':
    main()