from cyvcf2 import VCF

vcf_path = "/mnt/d/thesis/data/clinvar_20250323.vcf.gz"
output_bed = "/mnt/d/thesis/data/clinvar_bc_variants_for_vep.bed"

target_genes = {"BRCA1", "BRCA2", "TP53", "ATM", "CHEK2"}
allowed_clnsig = {
    "Likely_benign",
    "Pathogenic",
    "Benign/Likely_benign",
    "Benign",
    "Pathogenic/Likely_pathogenic",
    "Likely_pathogenic"
}

vcf_reader = VCF(vcf_path)

with open(output_bed, "w") as out:
    count = 0
    for variant in vcf_reader:
        if str(variant.INFO.get("CLNVC", "")).strip().lower() != "single_nucleotide_variant":
            continue
        geneinfo = variant.INFO.get("GENEINFO")
        if not geneinfo:
            continue
        gene = geneinfo.split(":")[0]
        if gene not in target_genes:
            continue
        clndn = str(variant.INFO.get("CLNDN", "")).lower()
        if "breast" not in clndn:
            continue
        clnsig = str(variant.INFO.get("CLNSIG", "")).strip()
        if clnsig not in allowed_clnsig:
            continue

        out.write(f"{variant.CHROM}\t{variant.start}\t{variant.end}\n")
        count += 1

print(f"✅ BED 区间写入完成，共 {count} 条")
