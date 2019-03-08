const colorByLevel = (x) => {
  if (x === 1) return '#112E51';
  if (x === 2) return '#0071BC';
  if (x === 3) return '#323A45';
  if (x === 4) return '#02BFE7';
  return '#000000';
}

export default colorByLevel;
