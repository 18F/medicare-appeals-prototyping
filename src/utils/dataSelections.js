import _ from 'lodash';

export const dataFilter = (data, category, filter) => {
  if (filter.selected === 'all') return data;

  return _.filter(data, record => {
    return record[category] === filter.selected
  })
}

export const getFieldCount = (data, groupBy, field, category, filter) => {
  const filtered = dataFilter(data, category, filter)

  const grouped = _.groupBy(filtered, record => {
    return record[groupBy]
  });

  return _.map(grouped, group => {
    return {
      [groupBy]: group[0][groupBy],
      [field]: _.sumBy(group, item => item[field])
    }
  });
}

export const getFieldAverage = (data, options, filter) => {
  const { groupBy, field, category, label } = options;
  const filtered = dataFilter(data, category, filter)

  const grouped = _.groupBy(filtered, record => {
    return record[groupBy]
  });

  return _.map(grouped, group => {
    return {
      [groupBy]: group[0][groupBy],
      [label]: _.meanBy(group, item => item[field])
    }
  })
}

export const getFieldAverageIgnoreZeroes = (data, options, filter) => {
  const { groupBy, field, category, label } = options;
  const filtered = dataFilter(data, category, filter)

  const grouped = _.groupBy(filtered, record => {
    return record[groupBy]
  });

  return _.map(grouped, group => {
    const zeroesIgnored = _.filter(group, item => item[field] !== 0);

    return {
      [groupBy]: group[0][groupBy],
      [label]: _.meanBy(zeroesIgnored, item => item[field])
    }
  })
}

export const getFieldsDifference = (data, options, filter) => {
  const { groupBy, minuend, subtrahend, category, difference } = options;
  const filtered = dataFilter(data, category, filter)

  const grouped = _.groupBy(filtered, record => {
    return record[groupBy]
  });

  return _.map(grouped, group => {
    return {
      [groupBy]: group[0][groupBy],
      [minuend]: _.sumBy(group, item => item[minuend]),
      [subtrahend]: _.sumBy(group, item => item[subtrahend])
    }
  }).map(record => {
    return {
      [groupBy]: record[groupBy],
      [difference]: _.subtract(record[minuend], record[subtrahend])
    }
  });
}

export const getMaxField = (data, groupBy, field, category) => {
  const grouped = getFieldCount(data, groupBy, field, category, {selected: 'all'});

  return _.maxBy(grouped, group => {
    return group[field]
  })[field];
}
