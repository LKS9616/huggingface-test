def translate(model, tokenizer, korean_text):
    tokenizer.src_lang = "ko_KR"
    encoded_ko = tokenizer(korean_text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_ko,
        forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
    )
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text