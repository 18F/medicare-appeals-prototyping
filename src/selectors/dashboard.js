import _ from 'lodash';

const dataFilter = (data, category, filter) => {
  if (filter.selected === 'all') return data;

  return _.filter(data, record => {
    return record[category] === filter.selected
  })
}

const selectData = (data, groupBy, field, category, filter) => {
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

const getMaxField = (data, groupBy, field, category) => {
  const grouped = selectData(data, groupBy, field, category, {selected: 'all'});

  return _.maxBy(grouped, group => {
    return group[field]
  })[field];
}

export default {
  selectData,
  getMaxField
}
