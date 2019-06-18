import queryString from 'query-string';

export const getDateRange = (start, end) => {
  const defaultRange = {
    start,
    end,
  };

  const parsed = queryString.parse(location.search);

  return Object.assign({}, defaultRange, parsed);
};
