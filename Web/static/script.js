const tools = ['encoding', 'encryption', 'hashing'];

const toolButtons = {
    encoding: document.getElementById('encoding_button'),
    encryption: document.getElementById('encryption_button'),
    hashing: document.getElementById('hashing_button')
};

const optionSections = {
    encoding: document.getElementById('encoding_options'),
    encryption: document.getElementById('encryption_options'),
    hashing: document.getElementById('hashing_options')
};

const encodeBtn = document.getElementById('encode_btn');
const decodeBtn = document.getElementById('decode_btn');
const inputText = document.getElementById('input_text');
const outputText = document.getElementById('output_text');
const outputArea = document.getElementById('output_area');
const submitBtn = document.getElementById('submit_btn');
const resultDescription = document.getElementById('result_description');

/* ====== Encryption Config Blocks ====== */
const encryptionConfigs = {
    aes: document.getElementById('aes_config'),
    fernet: document.getElementById('fernet_config'),
    rsa: document.getElementById('rsa_config'),
    utils: document.getElementById('utils_config')
};

/* ====== Hashing Config Blocks ====== */
const hashingConfigs = {
    sha: document.getElementById('sha_config'),
    blake2: document.getElementById('blake2_config'),
    salt: document.getElementById('salt_config'),
    pepper: document.getElementById('pepper_config')
};

/* ====== State ====== */
let activeTool = 'encoding';
let activeMode = 'encode';

/* ====== Tool Switching ====== */
function switchTool(tool) {
    activeTool = tool;

    tools.forEach(t => {
        toolButtons[t].classList.toggle('active', t === tool);
        optionSections[t].style.display = t === tool ? 'block' : 'none';
    });

    encodeBtn.style.display = tool === 'hashing' ? 'none' : 'block';
    decodeBtn.style.display = tool === 'hashing' ? 'none' : 'block';

    hideAllConfigs();
    outputArea.style.display = 'none';

    resultDescription.textContent =
        `You are using ${tool.charAt(0).toUpperCase() + tool.slice(1)} tool.`;
}

/* ====== Encode / Decode Switching ====== */
function switchMode(mode) {
    activeMode = mode;
    encodeBtn.classList.toggle('active', mode === 'encode');
    decodeBtn.classList.toggle('active', mode === 'decode');
    outputArea.style.display = 'none';
}

/* ====== Hide All Config Blocks ====== */
function hideAllConfigs() {
    Object.values(encryptionConfigs).forEach(el => el.style.display = 'none');
    Object.values(hashingConfigs).forEach(el => el.style.display = 'none');
}

/* ====== Encryption Option Handling ====== */
document
    .querySelectorAll("#encryption_options input[type='radio']")
    .forEach(radio => {
        radio.addEventListener('change', () => {
            hideAllConfigs();
            if (encryptionConfigs[radio.value]) {
                encryptionConfigs[radio.value].style.display = 'flex';
            }
        });
    });

/* ====== Hashing Option Handling ====== */
document
    .querySelectorAll("#hashing_options input[type='radio']")
    .forEach(radio => {
        radio.addEventListener('change', () => {
            hideAllConfigs();
            if (hashingConfigs[radio.value]) {
                hashingConfigs[radio.value].style.display = 'flex';
            }
        });
    });

/* ====== Tool Button Events ====== */
toolButtons.encoding.addEventListener('click', () => switchTool('encoding'));
toolButtons.encryption.addEventListener('click', () => switchTool('encryption'));
toolButtons.hashing.addEventListener('click', () => switchTool('hashing'));

/* ====== Encode / Decode Events ====== */
encodeBtn.addEventListener('click', () => switchMode('encode'));
decodeBtn.addEventListener('click', () => switchMode('decode'));

/* ====== Submit ====== */
submitBtn.addEventListener('click', async () => {
    const selectedRadio =
        document.querySelector(`#${activeTool}_options input[type='radio']:checked`);

    const payload = {
        tool: activeTool,
        mode: activeMode,
        input: inputText.value,
        option: selectedRadio ? selectedRadio.value : '',
        extra: {}
    };

    if (activeTool === 'encryption') {
        payload.extra = {
            aes_key: document.getElementById('aes_key')?.value || '',
            aes_mode: document.getElementById('aes_mode')?.value || '',
            fernet_key: document.getElementById('fernet_key')?.value || '',
            rsa_public: document.getElementById('rsa_public_key')?.value || '',
            rsa_private: document.getElementById('rsa_private_key')?.value || '',
            gen_key: document.getElementById('key_gen')?.checked || false,
            gen_iv: document.getElementById('iv_gen')?.checked || false
        };
    }

    if (activeTool === 'hashing') {
        payload.extra = {
            sha_type: document.getElementById('sha_type')?.value || '',
            blake2_type: document.getElementById('blake2_type')?.value || '',
            salt: document.getElementById('salt_value')?.value || '',
            pepper: document.getElementById('pepper_value')?.value || ''
        };
    }

    const response = await fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    const data = await response.json();
    outputText.value = data.result;
    outputArea.style.display = 'block';
});
