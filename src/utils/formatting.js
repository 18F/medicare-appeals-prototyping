export const capitalize = (val) => val.charAt(0).toUpperCase() + val.slice(1);

export const formatLabel = (val, char='_', replacement=' ') => capitalize(val).split(char).join(replacement);
