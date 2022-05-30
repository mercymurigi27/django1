const showSearch = document.querySelector('.search-icon');
const showFilter = document.querySelector('.filter-icon');
const searchForm = document.querySelector('.search');
const filterForm = document.querySelector('.filter'); 

const searchCat = document.querySelector('.submit-btn');
searchCat.disabled = true;

showSearch.addEventListener('click', () => {
    searchForm.style.display = 'flex';
    filterForm.style.display = 'none';
    showFilter.style.display = 'block';
    showSearch.style.display = 'none';

})

showFilter.addEventListener('click', () => {

    searchForm.style.display = 'none';
    filterForm.style.display = 'flex';
    showFilter.style.display = 'none';
    showSearch.style.display = 'block';


})


//input
const input = document.querySelector('#category');

input.addEventListener('change',(e)=>{

    if (e.target.value !== ''){
        searchCat.disabled = false;
    }
})


