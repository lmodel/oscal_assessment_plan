package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LocalDefinitions  {

  private List<SystemComponent> components;
  private List<InventoryItem> inventory-items;
  private List<SystemUser> users;
  private List<LocalObjective> objectives-and-methods;
  private List<Activity> activities;
  private String remarks;

}