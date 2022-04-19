from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_rankings,
                   reducer=self.reducer_count_rankings),
            MRStep(reducer=self.reducer_sorted_output)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer_count_ratings(self, key, values):
        yield key, sum(values)
        
    def mapper_get_rankings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1
        
    def reducer_count_rankings(self, key, values):
        yield str(sum(values)).zfill(5), key
        
    def reducer_sorted_output(self, count, movies):
        for movie in movies:
            yield movie, int(count)
        
        
if __name__ == '__main__':
    RatingsBreakdown.run()