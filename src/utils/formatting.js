import { format } from 'date-fns';

export const capitalize = (val) => val.charAt(0).toUpperCase() + val.slice(1);

export const formatLabel = (val, char='_', replacement=' ') => capitalize(val).split(char).join(replacement);

export const queryDate = (date) => format(date, 'YYYY-MM-DD');

export const readDate = (date) => format(date, 'MMM Do, YYYY');
