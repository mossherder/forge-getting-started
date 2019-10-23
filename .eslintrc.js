module.exports = {
    "extends": ["eslint:recommended", "google"],
    "parserOptions": {
        "ecmaVersion": 6,
        "sourceType": "module"
    },
    "env": {
        "jquery": true,
        "es6": true,
    },
    "rules": {
        "require-jsdoc": [0, {
            "require": {
                "FunctionDeclaration": false,
                "MethodDefinition": false,
                "ClassDeclaration": false
            }
        }],
        "max-len": "off",
        "no-console": "off",
        "valid-jsdoc": [0, {
            
        }],
    }
};
