import React from 'react';
import PropTypes from 'prop-types';

const SelectView = ({disabled, options, selected, title, setState}) => {
  const optionList = options.map((val, idx) => {
    return (
      <option value={val} key={`${val}-${idx}`}>
        {val.charAt(0).toUpperCase() + val.slice(1)}
      </option>
    );
  });

  return (
    <div className="ds-l-col--auto ">
        <label className="ds-c-label ds-u-margin--0" htmlFor="graph-select">
          <span className="ds-c-field__hint">{title}</span>
        </label>
        <select
          disabled={disabled}
          value={selected}
          className="ds-c-field ds-u-padding-y--0 ds-u-border--2"
          onChange={(e) => setState(e.target.value)}
        >
          { optionList }
        </select>
    </div>
  );
};

SelectView.propTypes = {
  disabled: PropTypes.bool,
  options: PropTypes.array,
  selected: PropTypes.string,
  title: PropTypes.string,
  setState: PropTypes.func,
}

SelectView.defaultProps = {
  disabled: false,
  options: ['option-1', 'option-2'],
  selected: 'option-1',
  title: 'Select Option',
  setState: (val) => console.log(val),
}

export default SelectView;
