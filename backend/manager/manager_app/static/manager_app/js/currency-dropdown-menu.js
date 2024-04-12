const root = document.documentElement;
const dropdownTitleIcon = document.querySelector(".dropdown-title-icon");
const dropdownTitle = document.querySelector(".dropdown-title");
const dropdownList = document.querySelector(".dropdown-list");
const mainButton = document.querySelector(".main-button");
const floatingIcon = document.querySelector(".floating-icon");

const icons = {
  uah: {
    path: "M226.8,197.6l-49.1,39.7h144.2v43.9h-187c-12.5,9.4-19.9,20.9-19.9,35.5c0,25.1,19.9,38.7,55.4,38.7c30.3,0,56.4-14.6,77.3-44.9l57.5,38.7c-31.3,48.1-87.8,72.1-141.1,72.1c-70,0-122.2-33.4-122.2-88.8c0-17.8,6.3-36.6,18.8-51.2H3.2v-43.9h91.9l50.2-39.7H3.2v-43.9h186c13.6-12.5,19.9-24,19.9-37.6c0-21.9-19.9-37.6-50.2-37.6c-29.3,0-54.3,16.7-72.1,44.9L31.4,85.8c30.3-48.1,79.4-72.1,132.7-72.1c72.1,0,119.1,37.6,119.1,88.8c0,18.8-6.3,37.6-16.7,51.2h55.4v43.9H226.8z",
    viewBox: "0 0 16 16"
  },
  eur: {
    path: "M4 9.42h1.063C5.4 12.323 7.317 14 10.34 14c.622 0 1.167-.068 1.659-.185v-1.3c-.484.119-1.045.17-1.659.17-2.1 0-3.455-1.198-3.775-3.264h4.017v-.928H6.497v-.936q-.002-.165.008-.329h4.078v-.927H6.618c.388-1.898 1.719-2.985 3.723-2.985.614 0 1.175.05 1.659.177V2.194A6.6 6.6 0 0 0 10.341 2c-2.928 0-4.82 1.569-5.244 4.3H4v.928h1.01v1.265H4v.928z",
    viewBox: "0 0 16 16"
  },
  usd: {
    path: "M4 10.781c.148 1.667 1.513 2.85 3.591 3.003V15h1.043v-1.216c2.27-.179 3.678-1.438 3.678-3.3 0-1.59-.947-2.51-2.956-3.028l-.722-.187V3.467c1.122.11 1.879.714 2.07 1.616h1.47c-.166-1.6-1.54-2.748-3.54-2.875V1H7.591v1.233c-1.939.23-3.27 1.472-3.27 3.156 0 1.454.966 2.483 2.661 2.917l.61.162v4.031c-1.149-.17-1.94-.8-2.131-1.718zm3.391-3.836c-1.043-.263-1.6-.825-1.6-1.616 0-.944.704-1.641 1.8-1.828v3.495l-.2-.05zm1.591 1.872c1.287.323 1.852.859 1.852 1.769 0 1.097-.826 1.828-2.2 1.939V8.73z",
    viewBox: "0 0 16 16"
  },
  gbp: {
    path: "M4 8.585h1.969c.115.465.186.939.186 1.43 0 1.385-.736 2.496-2.075 2.771V14H12v-1.24H6.492v-.129c.825-.525 1.135-1.446 1.135-2.694 0-.465-.07-.913-.168-1.352h3.29v-.972H7.22c-.186-.723-.372-1.455-.372-2.247 0-1.274 1.047-2.066 2.58-2.066a5.3 5.3 0 0 1 2.103.465V2.456A5.6 5.6 0 0 0 9.348 2C6.865 2 5.322 3.291 5.322 5.366c0 .775.195 1.515.399 2.247H4z",
    viewBox: "0 0 16 16"
  },
};

// const listItems = ["UAH - Українська гривня", "EUR - Євро", "USD - Долар США", "GBP - Фунти Стерлінги"];
const listItems = ["UAH", "EUR", "USD", "GBP"];

const iconTemplate = (path, viewBox) => {
  return `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}">
      <path d="${path}" />
    </svg>
  `;
};

// const iconTemplate = (path) => {
//   return `
//     <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
//       <path d="${path}" />
//     </svg>
//   `;
// };

const listItemTemplate = (currencyCode, translateValue) => {
    // const currencyName = translateValue;
    return `
    <li class="dropdown-list-item">
      <a href="javascript:void(0);" onclick="changeCurrency('${currencyCode}')" class="dropdown-button list-button" data-translate-value="${translateValue}%">
        <span class="text-truncate">${currencyCode}</span>
      </a>
    </li>
  `;
};

const renderListItems = () => {
  dropdownList.innerHTML += listItems
    .map((item, index) => {
      return listItemTemplate(item, 100 * index);
    })
    .join("");
};

window.addEventListener("load", () => {
  renderListItems();
});

const setDropdownProps = (deg, ht, opacity) => {
  root.style.setProperty("--rotate-arrow", deg !== 0 ? deg + "deg" : 0);
  root.style.setProperty("--dropdown-height", ht !== 0 ? ht + "rem" : 0);
  root.style.setProperty("--list-opacity", opacity);
};

mainButton.addEventListener("click", () => {
  const listWrapperSizes = 3.5; // margins, paddings & borders
  const dropdownOpenHeight = 4.6 * listItems.length + listWrapperSizes;
  const currDropdownHeight =
    root.style.getPropertyValue("--dropdown-height") || "0";

  currDropdownHeight === "0"
    ? setDropdownProps(180, dropdownOpenHeight, 1)
    : setDropdownProps(0, 0, 0);
});

dropdownList.addEventListener("mouseover", (e) => {
  const translateValue = e.target.dataset.translateValue;
  root.style.setProperty("--translate-value", translateValue);
});

dropdownList.addEventListener("click", (e) => {
  const clickedItemText = e.target.innerText.toLowerCase().trim();
  const clickedItemIcon = icons[clickedItemText];

  dropdownTitleIcon.innerHTML = iconTemplate(clickedItemIcon);
  dropdownTitle.innerHTML = clickedItemText;
  setDropdownProps(0, 0, 0);
});

dropdownList.addEventListener("mousemove", (e) => {
  const iconSize = root.style.getPropertyValue("--floating-icon-size") || 0;
  const x = e.clientX - dropdownList.getBoundingClientRect().x;
  const y = e.clientY - dropdownList.getBoundingClientRect().y;
  const targetText = e.target.innerText.toLowerCase().trim();
  const hoverItemText = icons[targetText];

  floatingIcon.innerHTML = iconTemplate(hoverItemText);
  root.style.setProperty("--floating-icon-left", x - iconSize / 2 + "px");
  root.style.setProperty("--floating-icon-top", y - iconSize / 2 + "px");
});
