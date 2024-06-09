let slotSymbols = [];
let m = 0;
let awascii32 = 'awjelyhosiumpcntbdfgr.,!{}_/;CTF';

let spinMode = 0;
let spinCounts = [0,0,0];
let slotIndices = [0,0,0];
let slotSpins = [0,0,0];
let ciphertextIndex = 0;

fetch('static/slotsymbols.txt')
.then(response => response.text())
.then(text => {
  slotSymbols = text.split(/(?:)/u);
  m = slotSymbols.length;
}).then(() => {
  playCoin(0);
  reset();
});


function change() {
  ciphertextIndex = (ciphertextIndex + 1) % 3;
  reset();
}


function reset() {
  if (ciphertextIndex == 0)       slotIndices = [10992, 30978, 12520];
  else if (ciphertextIndex == 1)  slotIndices = [30983,  7390,   481];
  else if (ciphertextIndex == 2)  slotIndices = [25974, 26744,  9122];
  spinCounts = [0,0,0];
  updatePlaintextDisplay();
  doSpinCleanup();
}


function spin() {
  const buttons = document.querySelectorAll('.button');
  buttons.forEach((b) => b.disabled = true);
  spinCounts[spinMode] += 1;
  updateModeDisplay();
  updatePlaintextDisplay();
  doSpinAnimation();
  for (let columnIndex = 0; columnIndex < 3; columnIndex++) {
    slotIndices[columnIndex] = (slotIndices[columnIndex] + slotSpins[columnIndex]) % m;
  }
  setTimeout(() => {
    doSpinCleanup();
    buttons.forEach((b) => b.disabled = false);
  }, 1800)
}


function playCoin(n){
  spinMode = n;
  if (n == 0)       slotSpins = [ 19,  22,  19];
  else if (n == 1)  slotSpins = [ 32,  27,  29];
  else if (n == 2)  slotSpins = [347, 349, 353];
  updateModeDisplay();
}


function updatePlaintextDisplay() {
  let decToAwascii32 = (x) => {return awascii32.charAt(x % 32) + awascii32.charAt((x >> 5) % 32) + awascii32.charAt((x >> 10) % 32)};
  document.getElementById('spinCount0').innerHTML = decToAwascii32(spinCounts[0]);
  document.getElementById('spinCount1').innerHTML = decToAwascii32(spinCounts[1]);
  document.getElementById('spinCount2').innerHTML = decToAwascii32(spinCounts[2]);
}









/**
 * 
 * NOTE: Everything below this point is purely visual and not needed to solve the challenge.
 * 
 */

function createSymbolElement(symbol) {
  const div = document.createElement('div');
  div.classList.add('symbol');
  div.textContent = symbol;
  return div;
}

function doSpinAnimation() {
  const slots = document.querySelectorAll('.slot');
  slots.forEach((slot, columnIndex) => {
    const symbols = slot.querySelector('.symbols');
    symbols.style.transition = 'none';
    symbols.style.top = '0';
    symbols.replaceChildren();
    for (let i = slotIndices[columnIndex]; i <= slotIndices[columnIndex] + slotSpins[columnIndex]; i++) {
      symbols.appendChild(createSymbolElement(slotSymbols[i % m]))
    }
    symbols.offsetHeight;
    symbols.style.transition = '';
    const symbolHeight = symbols.querySelector('.symbol')?.clientHeight;
    const offset = -(symbols.childElementCount - 1) * symbolHeight;
    symbols.style.top = `${offset}px`;
  });
}

function doSpinCleanup() {
  const slots = document.querySelectorAll('.slot');
  slots.forEach((slot, columnIndex) => {
    const symbols = slot.querySelector('.symbols');
    symbols.style.transition = 'none';
    symbols.style.top = '0';
    symbols.replaceChildren(createSymbolElement(slotSymbols[slotIndices[columnIndex]]));
    symbols.offsetHeight;
    symbols.style.transition = '';
  }); 
}

function updateModeDisplay() {
  document.getElementById('spinMode').innerHTML = spinMode;
}