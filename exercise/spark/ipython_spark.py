IPYTHON=1 IPYTHON_OPTS="--pylab" ./bin/pyspark  #用ipython 启动pyspark

user_data = sc.textFile("/PATH/ml-100k/u.user")

ages = user_fields.map(lambda x: int(x[1])).collect()
   hist(ages, bins=20, color='lightblue', normed=True)
   fig = matplotlib.pyplot.gcf()
   fig.set_size_inches(16, 10)

count_by_occupation = user_fields.map(lambda fields: (fields[3], 1)).
   reduceByKey(lambda x, y: x + y).collect()
   x_axis1 = np.array([c[0] for c in count_by_occupation])
   y_axis1 = np.array([c[1] for c in count_by_occupation])

   x_axis = x_axis1[np.argsort(y_axis1)]
   y_axis = y_axis1[np.argsort(y_axis1)]

   pos = np.arange(len(x_axis))
   width = 1.0
   ax = plt.axes()
   ax.set_xticks(pos + (width / 2))
   ax.set_xticklabels(x_axis)
   plt.bar(pos, y_axis, width, color='lightblue')
   plt.xticks(rotation=30)
   fig = matplotlib.pyplot.gcf()
   fig.set_size_inches(16, 10)


   count_by_occupation2 = user_fields.map(lambda fields: fields[3]).
   countByValue()
   print "Map-reduce approach:"
   print dict(count_by_occupation2)
   print ""
   print "countByValue approach:"
   print dict(count_by_occupation)

   def extract_title(raw):
     import re
     # this regular expression finds the non-word (numbers) between parentheses
     grps = re.search("\((\w+)\)", raw)
     if grps:
       # we take only the title part, and strip the trailing whitespace from the remaining text, below
       return raw[:grps.start()].strip()
     else:
        return raw

movie_data = sc.textFile("/PATH/ml-100k/u.item")
movie_fields = movie_data.map(lambda lines: lines.split("|"))
raw_titles = movie_fields.map(lambda fields: fields[1])

# In order to assign each term to an index in our vector, we need to create the term dictionary, which maps each term to an integer index
movie_titles = raw_titles.map(lambda raw_title:extract_title(raw_title))
title_terms = movie_titles.map(lambda t:t.split(" "))

idx = 0
   all_terms_dict = {}
   for term in all_terms:
     all_terms_dict[term] = idx
     idx +=1

#Spark's zipWithIndex
all_terms_dict2 = title_terms.flatMap(lambda x: x).distinct().
   zipWithIndex().collectAsMap()

# create a function that converts a set of terms into a sparse vector representation





