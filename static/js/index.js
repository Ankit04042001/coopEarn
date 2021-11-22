let dateHandler = document.querySelector('input[type="date"]');
let currentDate = new Date();
minExpiryDate = currentDate.getDate()+1;
minExpiryMonth = currentDate.getMonth()+1;
minExpiryYear = currentDate.getFullYear();
dateHandler.setAttribute('min',`${minExpiryYear}-${minExpiryMonth}-${minExpiryDate}`);

dateHandler.addEventListener('keypress',(e)=>{
  e.preventDefault();
});


const patterns = {
  pointCoupon : /^[0]{0,}?[1-9]$|^[0]{0,}?[1-9]\d$|^[0]{0,}?[1-4]\d{2}$|^[0]{0,}?[5-9]\d$/,
  serialNo : /^\d{6}$/,
  productName : /\w+/,
  denomination : /\w+/,
  quantity : /^[0]{0,}?[1-9]$|^[0]{0,}?\d{2}$|^[0]{0,}?[1][0][0]$/,
  dealerBenifit : /\w+/,
}

/************************** Form Validation ********************************/

const form = document.querySelector('form');
let inputs = document.querySelectorAll('input');
let submit = document.querySelector('button[type="submit"]');

function validateInputs(target, value){
    if (patterns[value].test(target.value)){
      target.classList.add("valid");
      target.classList.remove("invalid");

    }else{
      target.classList.add("invalid");
      target.classList.remove("valid");
    }
}

function validateForm(){
  for(let input of inputs){
    if(input.classList.contains("invalid")){
      return false;
    };
  }
  return true;
}




form.addEventListener('submit', (e)=>{
  console.log(validateForm());
  if(validateForm()==false){
    e.preventDefault();
  }
  else{
    submit.disabled = true;
  }
});



inputs.forEach((input)=>{
  input.addEventListener('keyup',(e)=>{
    if(e.target.attributes.name.value !== 'expiry'){
      validateInputs(e.target,e.target.attributes.name.value);
    }
  });
});



/************************ one time one click ****************************/



