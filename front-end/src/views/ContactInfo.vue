<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";

export default {
  name: "ContactInfo",
  components: {
    BaseInput,
    BaseButton
  },
  data() {
    return {
      isVisible: false
    }
  },
  methods: {
    openModal() {
      this.isVisible = true
    },
    closeModal() {
      this.isVisible = false
    }
  }
}

</script>

<template>
  <h2 class="my-4 text-md-center">📞 Almost there! Just enter everyone’s contact details! </h2>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <div class="card shadow">
        <div class="card-body">
          <form @submit.prevent>
            <!-- Host phone-number -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="host-phone-number"
                  label="Your number"
                  type="tel"
              />
            </div>

            <button
                class="btn add-contact px-0 d-flex align-items-center mx-auto"
                type="button"
                @click="openModal"
                data-bs-toggle="modal"
                data-bs-target="#addContact"
            >
                <svg class="rounded-circle plus me-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z" /><path d="M11 11V5h2v6h6v2h-6v6h-2v-6H5v-2z" /></svg>
              Add more contacts
            </button>

            <!-- Modal -->
            <div class="modal fade" :class="{ 'show d-block': isVisible }" id="addContact" tabindex="-1"
                 aria-labelledby="addContactLabel" aria-hidden="true">
              <div class="modal-dialog modal-sm modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title text-center text-primary" id="addContactLabel">Add Contact</h5>
                    <button type="button" class="btn-close" @click="closeModal" data-bs-dismiss="modal"
                            aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <BaseInput class="form-control" name="contact-name" label="Name" />
                    <BaseInput class="form-control" name="contact-phone-number" label="Phone number" />
                    <BaseButton type="button" class="btn-primary mt-4 py-2 w-75 text-white shadow-sm text-center"
                                label="Add" />
                  </div>
                </div>
              </div>
            </div>

            <Teleport to="body">
              <div v-show="isVisible" class="modal-backdrop fade show"></div>
            </Teleport>

            <div class="text-center">
              <BaseButton
                  class="btn-primary mt-4 py-2 w-75 text-white shadow-sm"
                  type="submit"
                  label="Continue"
              />
              <router-link
                  class="btn btn-back mt-3 py-2 w-75 mx-auto d-block shadow-sm"
                  to="/"
              >Go back</router-link>

            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.add-contact {
  width    : 100%;
  color    : $green;
  border: none;
  .plus {
    width: 40px;
    height: 40px;
    padding    : 5px;
    background : #E3F6EB;
    fill: $green;
    }
  }
</style>
