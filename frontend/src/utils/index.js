export const capitalize = (value) => {
  return value
    .trim()
    .toLowerCase()
    .split()
    .map((word) => word[0].toUpperCase() + word.substr(1))
    .join(" ");
};
