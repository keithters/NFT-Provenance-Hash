// Given the provided image_hashes.csv (from the Turf crew), this is an example JS script
// that let's you verify it yourself, assuming you have downloaded the images locally.

const crypto = require('crypto');
const fs = require('fs')

let foundBadMatches = false
let allImageHashes = ''

const hashFile = fs.readFileSync('./provenance_record.csv', 'utf8')

hashFile.split("\n").forEach( (row) => {
	const filename 		= row.split(',')[0]
	const image_hash 	= row.split(',')[1]
	if(filename == 'File Name'){ return; }// Skip the header

	if (filename) {
		const fileBuffer = fs.readFileSync(filename);
		const hashSum = crypto.createHash('sha256');
		hashSum.update(fileBuffer);
		const hex = hashSum.digest('hex');
		if(hex != image_hash){
			console.log(`❌: Hashes do not match for ${filename}!`)
		foundBadMatches = true
		}

		// Combine all the individual hashes so we can show the full provenance hash:
		allImageHashes = allImageHashes + hex
	}
})

if(!foundBadMatches){
  console.log("✅: All the individual image hashes matched!")
  const hashSum = crypto.createHash('sha256');
  hashSum.update(allImageHashes);
  console.log(`🖌️: Provenance Hash: ${hashSum.digest('hex')}`);
}

